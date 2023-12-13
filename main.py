from concurrent.futures import ProcessPoolExecutor
from Chrome import cards as chrome_cards, hampers as chrome_hampers, flowers as chrome_flowers
from Firefox import cards as firefox_cards, hampers as firefox_hampers, flowers as firefox_flowers


def run_cpu_tasks_in_parallel(tasks, url):
    with ProcessPoolExecutor() as executor:
        running_tasks = [executor.submit(task, url) for task in tasks]
        for running_task in running_tasks:
            running_task.result()


def task_1(url):
    chrome_flowers.order(url)


def task_2(url):
    chrome_hampers.order(url)


def task_3(url):
    chrome_cards.order(url)


def task_4(url):
    firefox_flowers.order(url)


def task_5(url):
    firefox_cards.order(url)


def task_6(url):
    firefox_hampers.order(url)


if __name__ == '__main__':
    try:
        url = input("Enter the URL for testing (do not include https://): ")
        run_cpu_tasks_in_parallel([
            task_1,
            task_2,
            task_3,
            task_4,
            task_5,
            task_6
        ], url)
    except Exception as e:
        print(f"End to End testing failed to run! ❌\nError: {e}")
