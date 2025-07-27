import sys
from multiprocessing import Pool, cpu_count
from time import perf_counter
from functools import reduce

sys.set_int_max_str_digits(10 ** 8)


def partial_factorial(start_end):
    """Обчислює частковий факторіал у заданому діапазоні."""
    start, end = start_end
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def compute_large_factorial(n):
    """Обчислює факторіал великого числа паралельно."""
    if n < 0:
        raise ValueError("Факторіал не визначений для від’ємних чисел.")

    num_workers = cpu_count()
    chunk_size = n // num_workers
    ranges = [(i * chunk_size + 1, (i + 1) * chunk_size) for i in range(num_workers)]
    ranges[-1] = (ranges[-1][0], n)  # Останній діапазон захоплює всі залишки

    with Pool(processes=num_workers) as pool:
        partial_results = pool.map(partial_factorial, ranges)

    return reduce(lambda x, y: x * y, partial_results)


if __name__ == "__main__":
    numbers = [50000, 100000]
    for num in numbers:
        start_time = perf_counter()
        result = compute_large_factorial(num)
        elapsed_time = perf_counter() - start_time
        print(f"{num}! обчислено за {elapsed_time:.4f} секунд")
