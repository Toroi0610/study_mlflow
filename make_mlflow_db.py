from os import chdir
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

import mlflow

# 2. make DataBase file

base_dir = Path("Sampling").absolute()
param_list = [f"param_{i}" for i in range(10)]

for directory in base_dir.iterdir():

    mlflow.start_run()
    mlflow.set_tag("Sampling_Points", directory.parts[-1])

    # Log a parameter (key-value pair)
    for param in param_list:
        with open(directory / param, mode="r") as f:
            mlflow.log_param(param, float(f.read()))

    # Log a metric; metrics can be updated throughout the run
    with open(directory / "metric", mode="r") as f:
        mlflow.log_metric("metric", float(f.read()))

    # Log an artifact (output file)
    fig, ax = plt.subplots()
    ax.imshow(np.random.randn(100, 100))
    plt.savefig("mosaic.png")
    plt.close()

    mlflow.log_artifact("mosaic.png")

    mlflow.end_run()
