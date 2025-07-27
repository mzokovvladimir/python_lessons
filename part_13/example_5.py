import threading
import time


lock = threading.BoundedSemaphore(2)


def worker(number):
    with lock:
        print(f'worker {number} thread is running')
        time.sleep(2)
        print(f'worker {number} thread is stopped')


thread1 = threading.Thread(target=worker, args=(20,))
thread2 = threading.Thread(target=worker, args=(7,))
thread3 = threading.Thread(target=worker, args=(20,))
thread4 = threading.Thread(target=worker, args=(7,))
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()