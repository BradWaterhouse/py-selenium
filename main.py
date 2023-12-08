from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from concurrent.futures import ProcessPoolExecutor
import time
from Chrome import cards as chrome_cards, hampers as chrome_hampers, flowers as chrome_flowers
from Firefox import cards as firefox_cards, hampers as firefox_hampers, flowers as firefox_flowers


def run_cpu_tasks_in_parallel(tasks):
    with ProcessPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()


def task_1():
    chrome_flowers.order()


def task_2():
    chrome_hampers.order()


def task_3():
    chrome_cards.order()


def task_4():
    firefox_flowers.order()


def task_5():
    firefox_cards.order()


def task_6():
    firefox_hampers.order()


if __name__ == '__main__':
        run_cpu_tasks_in_parallel([
            task_1,
            task_2,
            task_3,
            task_4,
            task_5,
            task_6
        ])
