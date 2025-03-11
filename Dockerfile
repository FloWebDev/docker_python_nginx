FROM python:3.13

WORKDIR /usr/src/app

RUN pip install --no-cache-dir --upgrade pip wheel

COPY ./flask/requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--reload", "-b", "0.0.0.0:5000", "hello:app"]
