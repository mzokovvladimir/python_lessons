import threading


lock = threading.Semaphore(2)

lock.acquire()
lock.release()
lock.release()

