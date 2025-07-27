import asyncio


async def micro_task_1():
    print("micro_task_1 start")


async def micro_task_2():
    print("micro_task_2 start")


async def macro_task():
    print("Macro Task start")
    asyncio.create_task(micro_task_1())
    asyncio.create_task(micro_task_2())
    await asyncio.sleep(1)
    print("Macro Task end")



async def main():
    print("main start")
    asyncio.create_task(macro_task())
    await asyncio.sleep(2)
    print("main end")


asyncio.run(main())