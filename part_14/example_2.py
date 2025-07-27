# async
import asyncio
import time


async def task(name, delay):
    print(f"Початок {name}")
    await asyncio.sleep(delay)
    print(f"Завершено {name}")


async def main():
    await asyncio.gather(
        task("Завдання 1", 2),
        task("Завдання 2", 2)
    )


start = time.time()
asyncio.run(main())
print(f"Час виконання: {time.time() - start:.2f} сек")
