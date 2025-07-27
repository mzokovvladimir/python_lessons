import asyncio


async def parse_params(future):
    await asyncio.sleep(0.1)
    params = {'user_id': 25}
    future.set_result(params)


async def select_from_db(future):
    params = await future
    print(f"Params: {params}")
    await asyncio.sleep(0.5)
    print("Done")


async def main():
    future = asyncio.Future()
    asyncio.create_task(parse_params(future))
    await select_from_db(future)


asyncio.run(main())