# 書類画像の向き補正 / Document Image Rotation Correction

## 背景 / Background

When working with scanned document images, we almost always have to make sure that they are correctly rotated in the right orientation, in order to proceed on to OCR models, layout analysis, etc. However, we've found that there was no established solution yet that is publicly available and easily accessible by everyone, to handle this problem, especially for Japanese document images. It is true that some methodologies like data-augmentation have been proven to enable a neural network to be invariant to spatial rotations, but it usually implies that the model has to be deeper enough to learn that, which we believe is not the most efficient solution. Therefore, the task is to detect the skewed rotations of any kind of given document images (incl. ones rotated upside down)

## 課題 / Task

To detect skewed rotation of document images, in multiples of 90 degree

### テストデータ / Data

(preparing...)
