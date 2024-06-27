# R-Bench
This repo is for the paper [Evaluating and Analyzing Relationship Hallucinations in Large Vision-Language Models (ICML2024)](https://www.bing.com/ck/a?!&&p=2f0bd6012a4f4b51JmltdHM9MTcxOTM2MDAwMCZpZ3VpZD0zMjgwNWY0Mi03YmRkLTZkYzEtMTdmNi00YzE3N2FiYjZjODUmaW5zaWQ9NTE4OQ&ptn=3&ver=2&hsh=3&fclid=32805f42-7bdd-6dc1-17f6-4c177abb6c85&psq=Evaluating+and+analyzing+relationship&u=a1aHR0cHM6Ly9hcnhpdi5vcmcvaHRtbC8yNDA2LjE2NDQ5djE&ntb=1).

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
