#!/bin/bash

CUDA_VISIBLE_DEVICES=6,7 python -m llava.eval.eval_rbench \
    --model-path pretrained_models/llava-v1.5-13b \
    --question-file data_filterd/image-level_filterd.json \
    --image-folder images \
    --answers-file outputs/image_result.json \
    --temperature 0 \
    --conv-mode vicuna_v1 \
    --qtype 'image-level' \

CUDA_VISIBLE_DEVICES=6,7 python -m llava.eval.eval_rbench \
    --model-path pretrained_models/llava-v1.5-13b \
    --question-file data_filterd/instance-level_filterd.json \
    --image-folder images \
    --answers-file outputs/instance_box_result.json \
    --temperature 0 \
    --conv-mode vicuna_v1 \
    --qtype 'instance-level-box' \

CUDA_VISIBLE_DEVICES=6,7 python -m llava.eval.eval_rbench \
    --model-path pretrained_models/llava-v1.5-13b \
    --question-file data_filterd/instance-level_filterd.json \
    --image-folder images \
    --answers-file outputs/instance_mask_result.json \
    --temperature 0 \
    --conv-mode vicuna_v1 \
    --qtype 'instance-level-mask' \
