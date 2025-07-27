import threading

counter = 0
lock = threading.RLock()


"""def task():
    print(f"Спроба встановити блокування")
    lock.acquire()
    print(f"Блокування отримано")

    print("Спроба встановити повторне блокування")
    lock.acquire()
    print("Розблокування")
    lock.release()
    lock.release()"""


def recursion_task(number):
    global counter
    if number < 0:
        return
    with lock:
        counter += 1
        print(f"Recursion: {number}, counter: {counter}")
        recursion_task(number - 1)


threads = [threading.Thread(target=recursion_task, args=(20,)) for _ in range(1)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)
