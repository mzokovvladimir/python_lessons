import threading


def print_numbers():
    total = 0
    for i in range(5000000):
        total += i
    print(total)


thread_1 = threading.Thread(target=print_numbers)
thread_2 = threading.Thread(target=print_numbers)
thread_3 = threading.Thread(target=print_numbers)
thread_4 = threading.Thread(target=print_numbers)
thread_1.start()
thread_2.start()
print(thread_2.is_alive())
thread_3.start()
thread_4.start()
thread_1.join()
print(thread_2.is_alive())
thread_2.join()
print(thread_2.is_alive())
thread_3.join()
thread_4.join()
print(thread_2.is_alive())
