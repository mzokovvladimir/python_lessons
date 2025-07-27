# sync
import time


def task(name, delay):
    print(f"Початок {name}")
    time.sleep(delay)
    print(f"Завершено {name}")


start = time.time()
task("Завдання 1", 2)
task("Завдання 2", 2)
print(f"Час виконання: {time.time() - start:.2f} сек")
