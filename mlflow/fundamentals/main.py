# Creating an MLflow Experiment and Log Data
import mlflow
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
import numpy as np


def main():
    print("Hello from MLflow fundamentals!")
    # set the Experiment name
    mlflow.set_experiment("Diabetes_Regression")

    # load datasets
    diabetes = load_diabetes()
    X, y = diabetes.data, diabetes.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # define hyper parameters
    learning_rate = 0.01
    n_iterations = 1000  # better coverage

    # Start a run
    with mlflow.start_run(run_name="SGD_Regression_Trial"):
        model = SGDRegressor(
            learning_rate="constant",
            eta0=learning_rate,
            max_iter=n_iterations,
            random_state=42,
            tol=1e-3,
        )

        model.fit(X_train, y_train)

        # Predict and calculate metric
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)

        # Log parameters
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("n_iterations", n_iterations)

        # Log the metric
        mlflow.log_metric("mse", mse)

        # Log the artifact (save a text file with model details)
        with open("model_summary.txt", "w") as f:
            f.write(
                f"Model: SGDRegressor\nMSE: {mse}\nLerning Rate: {learning_rate}\nIterations: {n_iterations}"
            )
        mlflow.log_artifact("model_summary.txt")

        print(f"Run completed with MSE: {mse}")


if __name__ == "__main__":
    main()
