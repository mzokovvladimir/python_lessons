import asyncio


async def parse_params(event, params_container):
    print("Start parsing params")
    await asyncio.sleep(0.1)
    params_container['params'] = {'user_id': 25}
    print("End parsing params")
    event.set()


async def select_from_db(event, params_container):
    print("Start selecting from db")
    await event.wait()
    params = params_container['params']
    print(f"Params: {params}")
    await asyncio.sleep(0.5)
    print("Done")


async def main():
    print("Start main")
    event = asyncio.Event()
    params_container = {}
    asyncio.create_task(parse_params(event, params_container))
    await select_from_db(event, params_container)
    print("End main")


asyncio.run(main())