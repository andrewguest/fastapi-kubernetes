FROM tiangolo/uvicorn-gunicorn:python3.8

WORKDIR /app

COPY ./requirements.txt /app
COPY ./app /app

RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /

# run gunicorn and bind to the public IP on port 8000 with 1 worker of type 'UvicornWorker'
ENTRYPOINT ["gunicorn", "app.main:app", "--bind", "0.0.0.0:8000", "-w", "1", "-k", "uvicorn.workers.UvicornWorker"]