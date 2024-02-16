FROM python:3.9

WORKDIR /cv-api

COPY ./requirements.txt /cv-api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /cv-api/requirements.txt

ENV OS docker

COPY ./src /cv-api/src

EXPOSE 80

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]