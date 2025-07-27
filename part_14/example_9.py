import asyncio


async def parse_params():
    await asyncio.sleep(0.1)
    return {'user_id': 25}


async def select_from_db():
    params = await asyncio.create_task(parse_params())
    print(f"Params: {params}")
    await asyncio.sleep(0.5)
    print("Done")


asyncio.run(select_from_db())