import threading
import time


def task(name, delay):
    print(f"Початок {name}")
    time.sleep(delay)
    print(f"Завершено {name}")


threads = []
start = time.time()
for i in range(2):
    t = threading.Thread(target=task, args=(f"Завдання {i + 1}", 2))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print(f"Час виконання: {time.time() - start:.2f} сек")
