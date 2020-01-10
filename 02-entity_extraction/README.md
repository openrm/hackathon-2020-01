# 鉄道乗車券画像からの情報抽出 / Entity Extraction from Train Ticket Images

## 背景 / Background

When we want to digitalize a document, we need to do actually two things:

  - extract the text contained in an image as characters (OCR)
  - label the content of the text and give it a signification within a document (labeling/classification)

To label the content, we can use natural language processing (based on text extracted with the OCR) and/or document layout analysis (based on the input image).


## 課題 / Task

The objective of this research is to extract the content of train tickets and correctly label it (origin station, destination station, price of the ticket, company, line, date of emission, date of validity, etc.)

### テストデータ / Data

The dataset contains around 150 images of train tickets. Some are scanned, some are photographed, but they are all in a relatively good quality (enough to apply OCR at least partially).

<details>
  <summary><b>Click here for examples</b></summary>
  <br />

  Labels:
  ```csv
  "origin","destination","line","company","price","issued_on","available_from","expire_on"
  "甲府","町田","はまかいじ号","JR","5190","2007-09-16","2007-09-16","2007-09-16"
  ```

  <img width="500" src="https://user-images.githubusercontent.com/20988826/72120090-15168900-339a-11ea-8f0b-aa9e7ac969d6.png" />

  <hr />

  Labels:
  ```csv
  "origin","destination","line","company","price","issued_on","available_from","expire_on"
  "立川","","中央ライナー","","510","2018-09-21","2018-09-21","2018-09-21"
  ```

  <img width="500" src="https://user-images.githubusercontent.com/20988826/72120119-324b5780-339a-11ea-958a-20eeee90145e.png" />

  <hr />

  Labels:
  ```csv
  "origin","destination","line","company","price","issued_on","available_from","expire_on"
  "","","","東京都交通局","1590","2019-01-13","2019-01-13","2019-01-13"
  ```

  <img width="500" src="https://user-images.githubusercontent.com/20988826/72120125-37a8a200-339a-11ea-8019-60ac290ca45f.png" />

  <hr />

  Labels:
  ```csv
  "origin","destination","line","company","price","issued_on","available_from","expire_on"
  "池袋","所沢","","西武鉄道","400","2018-12-23","2018-12-23","2018-12-23"
  ```

  <img width="500" src="https://user-images.githubusercontent.com/20988826/72120137-3ecfb000-339a-11ea-95f6-16e68915a843.png" />

  <hr />

  Labels:
  ```csv
  "origin","destination","line","company","price","issued_on","available_from","expire_on",""
  "三田","尼崎","","","630","2011-03-25","2011-03-25","2011-03-25"
  ```

  <img width="500" src="https://user-images.githubusercontent.com/20988826/72120140-43946400-339a-11ea-85e2-bbe7c77853ea.png" />

  <hr />

  ```csv
  "origin","destination","line","company","price","issued_on","available_from","expire_on"
  "盛岡","東京","新幹線","JR","14240","2012-10-07","2012-10-08","2012-10-08"
  ```

  <img width="500" src="https://user-images.githubusercontent.com/20988826/72120146-4bec9f00-339a-11ea-9103-de80805934ae.png" />
</details>

### 提出 / Submission

We ask to submit a script to predict values for the entities from the test images, that will be downloaded under `data/test` during the CI pipeline. The results must be formatted in a specified way so that we can evaluate it.

Thus, the script has to:

 - walk through the directory `data/test`, and load found images (named `*.png`)
 - extract the content of the image as text and classify it
 - output to the standard output the results and the original file names in CSV format (see below)

### 出力例 / Sample Output

Stdout must return a result formatted as:
```csv
filename,origin,destination,line,company,price,issued_on,available_from,expire_on
1.png,都区内,都区内,,JR,730,2010-01-19,2010-01-19,2010-01-19
2.png,甲府,町田,はまかいじ号,JR,5190,2007-09-16,2007-09-16,2007-09-16
4.png,町田,土合,楊浜線,JR,3570,2007-11-04,2007-11-23,2007-11-25
5.png,水上,大宮,EL&SL奥利根号,JR,510,2007-11-04,2007-11-23,2007-11-23
```
