FROM tensorflow/tensorflow:2.0.0-py3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD . .

ENTRYPOINT ["python", "predict.py"]
