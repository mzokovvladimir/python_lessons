import time


class TimerContextManager:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time() 
        execution_time = self.end_time - self.start_time
        print(f"Час виконання: {execution_time:.4f} секунд")


with TimerContextManager():
    total = 0
    for i in range(1, 10_000_000):
        total += i
    print("Сума:", total)
