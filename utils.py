
import os
import math
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt


colors = {'red': (250, 0, 45, 120), 'green': (100, 250, 0, 120), 'blue': (0, 40, 250, 120), 'gold':(255, 215, 0, 120), 'pink':(255,105,180, 120)}

def show_mask(mask, ax, random_color=False, color=None):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        # color = np.array([30/255, 144/255, 255/255, 0.6])
        color = np.array(color) / 255
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)

def show_mask_pil(mask, random_color=False, color=None):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array(color) / 255

    # print(mask.shape)
    # print(mask)
    h, w = mask.shape[-2:]
    mask_image = (mask.reshape(h, w, 1) * color.reshape(1, 1, -1) * 255).astype(np.uint8)

    # Create a transparent RGBA image with the mask applied as the alpha channel
    rgba_image = np.zeros((h, w, 4), dtype=np.uint8)
    rgba_image[:, :, :3] = mask_image[:, :, :3]
    rgba_image[:, :, 3] = mask_image[:, :, 3]

    # Convert the NumPy array to a PIL Image
    pil_image = Image.fromarray(rgba_image, 'RGBA')

    return pil_image


def show_box(box, ax, label=None, color=None):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor=color, facecolor=(0,0,0,0), lw=2)) 
    if label:
        ax.text(x0, y0, label)


def draw_mask(image_folder, image_file, line, colors, sub_color='red', obj_color='green'):
    image = Image.open(os.path.join(image_folder, image_file)).convert('RGBA')
    mask_file = 'dataset/instance_mask/' + '{}.png'.format(line['question_id']) 
    mask = Image.open(mask_file)
    resized_mask_image = mask.resize(image.size, resample=Image.NEAREST)
    resized_mask = np.array(resized_mask_image)
    # print(resized_mask[np.nonzero(resized_mask)])
    # print((resized_mask==1).any())
    sub_mask = np.zeros_like(resized_mask)
    sub_mask[resized_mask==1] = 1
    obj_mask = np.zeros_like(resized_mask)
    obj_mask[resized_mask==2] = 1
    
    sub_mask_image = show_mask_pil(sub_mask, color=colors[sub_color])
    obj_mask_image = show_mask_pil(obj_mask, color=colors[obj_color])
    image.paste(sub_mask_image, (0, 0), sub_mask_image)
    image.paste(obj_mask_image, (0, 0), obj_mask_image)
    return image

def draw_box(image_folder, image_file, line, colors, sub_color='red', obj_color='green'):      
    image = Image.open(os.path.join(image_folder, image_file)).convert('RGB')
    w, h = image.size
    draw = ImageDraw.Draw(image)
    # bbox = [bbox[0], bbox[1], bbox[0] + bbox[2], bbox[1] + bbox[3]]
    sub_box, obj_box = line['sub_box'], line['obj_box']
    sub_box = [b * x for b, x in zip(sub_box, [w, h, w, h])]
    obj_box = [b * x for b, x in zip(obj_box, [w, h, w, h])]
    draw.rectangle(sub_box, outline=sub_color, width=4)
    draw.rectangle(obj_box, outline=obj_color, width=4)
    return image

def instance_qs_construct(line, type='mask', sub_color='red', obj_color='green'):
    qs = line["text"]
    sub, obj = line['subject'], line['object']
    mode = 'mask' if type == 'mask' else 'bounding box'

    qs = qs.replace(sub.lower(), sub.lower() + ' in {} {}'.format(sub_color, mode))
    qs = qs.replace(obj.lower(), obj.lower() + ' in {} {}'.format(obj_color, mode))
    return qs
