import threading


lock = threading.BoundedSemaphore(2)

lock.acquire()
lock.release()
lock.release()
