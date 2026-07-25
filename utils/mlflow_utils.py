from pathlib import Path
import mlflow

PROJECT_ROOT = Path(__file__).resolve().parent
DB_PATH = PROJECT_ROOT / "mlflow.db"


def start_run(
    run_name: str,
    experiment_name: str = "Sales_Forecasting_FreshRetailNet-50K Dataset"
):
    mlflow.set_tracking_uri(f"sqlite:///{DB_PATH}")

    if mlflow.active_run() is not None:
        mlflow.end_run()

    mlflow.set_experiment(experiment_name)

    mlflow.start_run(
        run_name=run_name,
        nested=False
    )


def end_run():
    if mlflow.active_run() is not None:
        mlflow.end_run()