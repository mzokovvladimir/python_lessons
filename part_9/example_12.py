from contextlib import contextmanager
import time


@contextmanager
def timer():
    start_time = time.time()
    try:
        yield  # Виконання блоку коду всередині `with`
    finally:
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання: {execution_time:.4f} секунд")


with timer():
    total = 0
    for i in range(1, 10_000_000):
        total += i
    print("Сума:", total)
