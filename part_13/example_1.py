import threading
import time

def print_numbers():
    total = 0
    for i in range(5000000):
        total += i
    print(total)


start_time = time.time()
thread_1 = threading.Thread(target=print_numbers)
thread_1.start()
thread_1.join()
print(f"Result1: {time.time() - start_time}")
thread_2 = threading.Thread(target=print_numbers)
thread_2.start()
thread_2.join()
print(f"Result2: {time.time() - start_time}")

start_time = time.time()
print_numbers()
print(f"Result3: {time.time() - start_time}")