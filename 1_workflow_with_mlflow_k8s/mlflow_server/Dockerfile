FROM python:3.8-slim-buster

WORKDIR /mlflow

RUN pip install mlflow psycopg2-binary boto3

EXPOSE 5000

CMD ["mlflow", "server", \
     "--host", "0.0.0.0", \
     "--port", "5000", \
     "--backend-store-uri", "postgresql://mlflow:mlflow@postgres/mlflow", \
     "--default-artifact-root", "s3://my-coder-bucket-1", \
     "--artifacts-destination", "s3://my-coder-bucket-1"]
