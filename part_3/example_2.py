from math import ceil
from inspect import isgenerator
from typing import Generator


def prime_generator(end: int) -> Generator[int, None, None]:
    """
    Generates prime numbers up to the given end value.

    Args:
        end: The upper limit for prime number generation.

    Yields:
        Prime numbers found within the given range.
    """
    value = 2
    while value <= end:
        value_end = ceil(value / 2)
        for i in range(2, value_end + 1):
            if (value % i) == 0:
                break
        else:
            yield value
        value += 1


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
