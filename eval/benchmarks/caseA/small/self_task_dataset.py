import os
import sys

PROJECT_NAME = 'RayCloudSim'
cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = cur_path
while os.path.split(os.path.split(root_path)[0])[-1] != PROJECT_NAME:
    root_path = os.path.split(root_path)[0]
root_path = os.path.split(root_path)[0]
sys.path.append(root_path)

import random

ROOT_PATH = 'eval/benchmarks/caseA/small'


def main():
    # 1. tasks
    generated_time = random.choices(range(1000), k=500)
    generated_time.sort()
    simulated_tasks = []
    for i, t in enumerate(generated_time):
        simulated_tasks.append(
            (t, # generated_time
             [i,  # task_id
              random.randint(10, 100),  # task_size
              random.randint(1, 10),  # cycles_per_bit
              random.randint(20, 80),  # trans_bit_rate
              random.randint(50, 100),  # ddl
              f'n{random.randint(0, 19)}',  # src_name
              f't{i}']) # task_name
        )
    
    # 2. saving
    if not os.path.exists(f"{ROOT_PATH}/tasks.txt"):
        with open(f"{ROOT_PATH}/tasks.txt", 'w+') as fw:
            fw.write(str(simulated_tasks))
    else:
        print("File already exists!")

    # 3. loading
    with open(f"{ROOT_PATH}/tasks.txt", 'r') as fr:
        simulated_tasks = eval(fr.read())


if __name__ == '__main__':
    main()