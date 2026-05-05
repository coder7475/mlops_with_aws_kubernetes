# Fundamentals

## What is MLflow?

MLflow is an open-source platform designed to manage the machine learning lifecycle, from experiment tracking to model deployment. It offers a suite of tools for tracking experiments, packaging projects, and deploying models, making the entire ML process more efficient and collaborative.

## Components of MLflow

1. **MLflow Tracking**: Tracks experiments, parameters, metrics, and artifacts associated with machine learning models.

1. **MLflow Projects**: Packages machine learning code into a reusable and reproducible format.

1. **MLflow Models**: Provides a standard format for packaging machine learning models for deployment.

1. **MLflow Model Registry**: Centralizes model management and governance by tracking model versions, stages and allows for collaborations.

## Applications

- Reproducibility: Ensures that experiments can be reproduced by tracking all necessary information, including code versions and datasets.

- Experiment Tracking: Logs and compares different model training runs, helping identify the best-performing model based on specific criteria.

- Performance Comparison: Allows for easy comparison of model performance over time and across different runs.

- Code Sharing: Facilitates sharing of ML code with other data scientists or teams, promoting collaboration and knowledge transfer.

- Model Deployment: Simplifies the process of deploying models to various platforms, including real-time serving through REST APIs or batch inference on Apache Spark.

- Model Packaging: Provides a standardized way to package models for different environments, ensuring consistency and portability.

- Model Versioning: Keeps track of different versions of a model, allowing for easy rollback to previous versions if needed.

# Launch MLflow

```
uv run mlflow server \
  --host 0.0.0.0 \
  --port 5000 \
  --allowed-hosts '*' \

```
