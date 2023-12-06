from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from concurrent.futures import ProcessPoolExecutor
import time
import flowers
import hampers
import cards


def run_cpu_tasks_in_parallel(tasks):
    with ProcessPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()


def task_1():
    flowers.order()


def task_2():
    hampers.order()


def task_3():
    cards.order()


if __name__ == '__main__':
    run_cpu_tasks_in_parallel([
        task_1,
        task_2,
        task_3
    ])
