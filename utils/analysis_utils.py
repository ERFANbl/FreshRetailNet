import mlflow


def log_metrics(metrics: dict):
    mlflow.log_metrics(metrics)


def log_table(df, artifact_file: str):
    mlflow.log_table(df, artifact_file)


def log_figure(fig, artifact_file: str):
    mlflow.log_figure(fig, artifact_file)


def log_text(text: str, artifact_file: str):
    mlflow.log_text(text, artifact_file)