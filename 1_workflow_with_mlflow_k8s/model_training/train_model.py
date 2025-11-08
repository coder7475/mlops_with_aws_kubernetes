import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
import json

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("s3://my-coder-bucket-1/k8s_synthetic_classification_workflow")

def generate_synthetic_data(n_samples=1000):
    np.random.seed(42)
    X = np.random.randn(n_samples, 10)
    y = (X[:, 0] + X[:, 1] ** 2 + np.sin(X[:, 2]) + np.random.randn(n_samples) > 0).astype(int)

    row_indices = np.random.choice(n_samples, 100)
    col_indices = np.random.choice(10, 100)
    X[row_indices, col_indices] = np.nan

    return pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)]), pd.Series(y, name='target')

def train_model():
    X, y = generate_synthetic_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run():
        n_estimators = 100
        max_depth = 5
        min_samples_split = 2

        # Create a pipeline with SimpleImputer and RandomForestClassifier
        pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='mean')),
            ('rf', RandomForestClassifier(n_estimators=n_estimators,
                                          max_depth=max_depth,
                                          min_samples_split=min_samples_split,
                                          random_state=42))
        ])

        # Fit the pipeline
        pipeline.fit(X_train, y_train)

        # Make predictions
        predictions = pipeline.predict(X_test)
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)

        # Log parameters
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("min_samples_split", min_samples_split)
        mlflow.log_param("imputer_strategy", "mean")

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)

        # Log the model
        mlflow.sklearn.log_model(pipeline, "random_forest_model")

        # Log feature importance
        feature_importance = dict(zip(X.columns, pipeline.named_steps['rf'].feature_importances_))
        with open("feature_importance.json", "w") as f:
            json.dump(feature_importance, f)
        mlflow.log_artifact("feature_importance.json", "feature_importance")

        # Log the dataset
        X.to_csv("synthetic_data.csv", index=False)
        mlflow.log_artifact("synthetic_data.csv", "dataset")

        # Log the code
        mlflow.log_artifact("train_model.py", "code")

    print(f"Model metrics: accuracy={accuracy}, precision={precision}, recall={recall}, f1_score={f1}")
    print("Experiment logged in MLflow")

if __name__ == "__main__":
    train_model()
