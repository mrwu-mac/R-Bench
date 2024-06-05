#!/bin/bash
### eval_image
python eval_pope.py \
    --annotation-dir dataset \
    --question-file dataset/nocaps/question_v1.json \
    --question-id-file dataset/nocaps/question_v1_image_ids_holder.json \
    --result-file output/qwen/question_v1_out.json \
    --error-file output/qwen/question_v1_error.json \
    --eval_image


### eval_instance
python eval_pope.py \
    --annotation-dir dataset \
    --question-file dataset/nocaps/instance-level_filterd.json \
    --question-id-file dataset/nocaps/instance-level_ids_holder.json \
    --result-file output/instructblip_13b/question_v2_local_so_r_out_box_color_shift.json \
    --error-file output/instructblip_13b/question_v2_local_so_r_out_mask_error.json \
    --eval_instance

### eval_box
# python eval_pope.py \
#     --annotation-dir dataset \
#     --question-file output/qwen/coco_v1_boudning_box_out.json \
#     --result-file output/qwen/coco_v1_boudning_box_out.json \
#     --eval_box 


# #### eval_pope_obj
# python eval_pope.py \
#     --annotation-dir dataset \
#     --question-file dataset/nocaps/nocaps_pope_obj_random.json \
#     --question-id-file dataset/nocaps/question_pope_obj_ids_holder.json\
#     --result-file output/qwen/nocaps_pope_obj_random_out.json \
#     --eval_obj

# #### eval_web
# python eval_pope.py \
#     --annotation-dir dataset \
#     --question-file dataset/web/web_v1.json \
#     --result-file output/llava1.5_13b/web_v1_out.json \
#     --eval_image \
#     --eval_web

