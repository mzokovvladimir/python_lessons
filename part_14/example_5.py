import asyncio


async def macro_task():
    print("Begin")
    await asyncio.sleep(1)
    print("End")


asyncio.run(macro_task())
