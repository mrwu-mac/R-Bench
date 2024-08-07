# R-Bench
![teaser](assets/r-bench.png)

This repo is for the paper [Evaluating and Analyzing Relationship Hallucinations in Large Vision-Language Models (ICML2024)](https://www.bing.com/ck/a?!&&p=2f0bd6012a4f4b51JmltdHM9MTcxOTM2MDAwMCZpZ3VpZD0zMjgwNWY0Mi03YmRkLTZkYzEtMTdmNi00YzE3N2FiYjZjODUmaW5zaWQ9NTE4OQ&ptn=3&ver=2&hsh=3&fclid=32805f42-7bdd-6dc1-17f6-4c177abb6c85&psq=Evaluating+and+analyzing+relationship&u=a1aHR0cHM6Ly9hcnhpdi5vcmcvaHRtbC8yNDA2LjE2NDQ5djE&ntb=1).

```
@inproceedings{
wu2024evaluating,
title={Evaluating and Analyzing Relationship Hallucinations in Large Vision-Language Models},
author={Mingrui Wu and Jiayi Ji and Oucheng Huang and Jiale Li and Yuhang Wu and Xiaoshuai Sun and Rongrong Ji},
booktitle={Forty-first International Conference on Machine Learning},
year={2024},
url={https://openreview.net/forum?id=xpSlt67vxQ}
}
```


## Data
Download [R-Bench](https://drive.google.com/file/d/1MIFFhFWIMbk44yQGAxvd_0dM1dAnYEmu/view?usp=sharing).
The main annotation files include:
```
- image-level_filterd.json
- instance-level_filterd.json
- nocaps_pope_obj_random_image.json
- nocaps_pope_obj_popular_image.json
- nocaps_pope_obj_adversarial_image.json
- web_data
```
These files contain annotations for image-level, instance-level, pope-object, and web-data questions. For image-level and instance-level questions, we randomly sampled five subsets into the `[type]_ids_[subset].json` files.

Download the images from [Open Image validation set (v4)](https://storage.googleapis.com/openimages/web/download_v7.html).

## Eval
To run LVLM on R-Bench using the official inference script of the LVLMs, and format the result file as follows:
```
{"question_id": 0, "text":[model output]}
{"question_id": 1, "text":[model output]}
...
```
Tips: We provide instance-level question tools in `utils.py`. Please use the `draw_mask` and `draw_box` functions to draw the mask and box on input images, respectively. Additionally, use the `instance_qs_construct` function to reformat the instance questions.

And eval with,
```
sh eval.sh
```

## Acknowledge
The evaluation code is based on [POPE](https://github.com/AoiDragon/POPE).
