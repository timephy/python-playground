import asyncio


async def func(arg):
    while True:
        print('func', arg)
        await asyncio.sleep(1)
        if arg == 2:
            raise Exception


loop = asyncio.new_event_loop()

# loop.run_until_complete(func())
t1 = loop.create_task(func(1))
t2 = loop.create_task(func(2))

print(t1)
print(t2)

# t1.cancel()

print("Tasks:", len(asyncio.all_tasks(loop)))

loop.run_forever()
