# R-Bench
This repo is for the paper Evaluating and Analyzing Relationship Hallucinations in Large Vision-Language Models (ICML2024).

![teaser](assets/r-bench.png)

## Data
Download [R-Bench](https://drive.google.com/file/d/1MIFFhFWIMbk44yQGAxvd_0dM1dAnYEmu/view?usp=sharing)

Download the images from [Open Image](https://storage.googleapis.com/openimages/web/download_v7.html).

## Eval
Run LVLM on R-Bench, the instance-level question tools in ```utils.py```, use function ```draw_mask``` and ```draw_box``` to draw the mask and box respectively.

And eval with,
```
sh eval.sh
```
