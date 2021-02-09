# WordDetection-Data-Generator
[![Build Status][travis-image]][travis]
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/27b8735c675640878aeb603654cdf57f)](https://app.codacy.com/gh/robinreni96/WordDetection-Data-Generator?utm_source=github.com&utm_medium=referral&utm_content=robinreni96/WordDetection-Data-Generator&utm_campaign=Badge_Grade)

[travis-image]: https://www.travis-ci.com/robinreni96/WordDetection-Data-Generator.svg?branch=main
[travis]: https://www.travis-ci.com/github/robinreni96/WordDetection-Data-Generator

This python script will generate n pages of words with bbox and its ground truth labels. Also it supports various background colors, fonts etc. Additionally it can export the dataset as tfrecord

<p align="center"> 
<img src="https://github.com/robinreni96/WordDetection-Data-Generator/blob/main/Word_Dataset.jpg">
</p>

## Compatibility
The code is tested and developed  in **Ubuntu 20.04** and using **Pyton 3.8**.But the code has the realiability to run on most of the configuration . If you face issues , do open up an issue for this repo .All the package dependencies are mentioned in **requirements.txt**.

## Arguments
```
For Word Generator
------------------
--output_dir: The datset images to be stored (default: dataset/)
--input_file: Text file contain random words for generator dataset pages
--background: Background Color (default: white)
--font_dir: Fonts to be used for generating dataset (default: fonts/)
--num_pages: Number of images of dataset need to be generated (default: 10)
--width: Width of the image (default: 600) in pixel
--height: Height of the image (default: 800) in pixel

For TFRecord Generator
----------------------
--csv_input: Ground truth labels csv file (default: ground_truth.csv)
--output_path: Location for tfrecord file need to be saved (default: dataset.tfrecord)
--dataset_dir: Dataset dir need to be used for images (default: dataset/)
```

## Get Started
1. Install python 3.8 and requirements.txt to install the necessary dependencies
2. To run the word detection generator.
   ```python insert_word.py --input_file words.txt --num_pages 100```
3. The dataset will be stored in ```dataset``` folder  and the coordinates, ground truth values will be save in ``` ground_truth.csv```
4. To export as tfrecord file, ```python generate_tfrecord.py```
5. To check the bbox drawn in image use ```cv_doc.py```
6. Enjoy the dataset

## Sample Image of Dataset
<p align="center"> 
<img src="https://github.com/robinreni96/WordDetection-Data-Generator/blob/main/sample.jpg">
</p>

<a href="https://www.buymeacoffee.com/robinreni96" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 20px !important;width: 80px !important;" ></a>

Copyright © 2021 Robin Reni. All rights reserved
   

