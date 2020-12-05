from os import chdir
from pathlib import Path
from uuid import uuid4
from random import random


base_dir = Path("Sampling").absolute()
base_dir.mkdir(exist_ok=True)
param_list = [f"param_{i}" for i in range(10)]

for i in range(100):
    exp_dir = base_dir / ("point_" + str(i))
    exp_dir.mkdir()
    chdir(exp_dir)
    
    param_value = [random() for _ in range(10)]
    for param, value in zip(param_list, param_value):
        with open(param, mode="w") as f:
            f.write(str(value))
    
    metric = sum(param_value)
    with open("metric", mode="w") as f:
        f.write(str(metric))
