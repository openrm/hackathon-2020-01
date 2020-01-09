# 書類画像の向き補正 / Document Image Rotation Correction

## 背景 / Background

When working with scanned document images, we almost always have to make sure that they are correctly rotated in the right orientation, in order to proceed on to OCR models, layout analysis, etc. However, we've found that there was no established solution yet that is publicly available and easily accessible by everyone, to handle this problem, especially for Japanese document images. It is true that some methodologies like data-augmentation have been proven to enable a neural network to be invariant to spatial rotations, but it usually implies that the model has to be deeper enough to learn that, which we believe is not the most efficient solution. Therefore, the task is to detect the skewed rotations of any kind of given document images.

One difficult problem to solve, is to identify in wich direction is a text document. If a document is rotated with an angle of 180, how the computer can detect efficiently that the text is up-side down ?

## 課題 / Task

The objective of this research is to detect skewed rotation of document images, in multiples of 90 degree. 

### テストデータ / Data

There is around 3000 images in the dataset, each one of them is rotated in a specific angle (multiple of 90).

The submissions will be tested against this dataset.

### 提出 / Submission

We ask to submit a script to predict the rotations for the test images, that will be downloaded under `data/test` during the CI pipeline. The results must be formatted in a specified way so that we can evaluate it.

Thus, the script has to:

 - walk through the directory `data/test`, and load found images (named `*.png` or `*.jpg`)
 - predict the rotation angle for each image (0, 90, 180, 260)
 - output to the standard output the results and the original file names in CSV format (see below)

### 出力例 / Sample Output

Stdin must return a result formatted as:
```csv
filename,label
001.png,90
002.png,0
abcd.png,260
...
```
