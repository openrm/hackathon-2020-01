# 鉄道乗車券画像からの情報抽出 / Entity Extraction from Train Ticket Images

## 背景 / Background

When we want to digitalize a document, we need to do actually two things:
  - extract the text contained in an image as characters (OCR)
  - label the content of the text and give it a signification within a document (labeling/classification)

To label the content, we can use natural language (based on text extracted with the OCR) and/or document layout analysis (based on the input image).


## 課題 / Task

The objective of this research is to extract the content of train tickets and correctly label it (origin station, destination station, price of the ticket, company, line, date of emission, date of validity, etc.)

### テストデータ / Data

The dataset contains around 150 images of train tickets. Some are scanned, some are photographed, but they are all in a relatively good quality (enough to apply OCR at least partially).

### 提出 / Submission

We ask to submit a script to predict the rotations for the test images, that will be downloaded under `data/test` during the CI pipeline. The results must be formatted in a specified way so that we can evaluate it.

Thus, the script has to:

 - walk through the directory `data/test`, and load found images (named `*.png`)
 - extract the content of the image as text and classify it
 - output to the standard output the results and the original file names in CSV format (see below)

### 出力例 / Sample Output

Stdin must return a result formatted as:
```csv
filename,origin,destination,line,company,price,issued_on,available_from,expire_on,
1.png,都区内,都区内,,JR,730,2010-01-19,2010-01-19,2010-01-19,  
2.png,甲府,町田,はまかいじ号,JR,5190,2007-09-16,2007-09-16,2007-09-16,  
4.png,町田,土合,楊浜線,JR,3570,2007-11-04,2007-11-23,2007-11-25,
5.png,水上,大宮,EL&SL奥利根号,JR,510,2007-11-04,2007-11-23,2007-11-23,
```
