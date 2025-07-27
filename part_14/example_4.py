import multiprocessing
import time


def task(name, delay):
    print(f"Початок {name}")
    time.sleep(delay)
    print(f"Завершено {name}")


if __name__ == "__main__":
    processes = []
    start = time.time()
    for i in range(2):
        p = multiprocessing.Process(target=task, args=(f"Завдання {i + 1}", 2))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    print(f"Час виконання: {time.time() - start:.2f} сек")
