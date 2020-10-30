import asyncio

loop = asyncio.get_event_loop()


async def run():
    while True:
        # sleep forever by 1 hour intervals
        await asyncio.sleep(3600)


try:
    try:
        try:
            try:
                loop.run_until_complete(run())
            except KeyboardInterrupt:
                print('ASFDGAIFGASIDASDA')
                pass
            finally:
                loop.close()
        except KeyboardInterrupt:
            print(3)
    except KeyboardInterrupt:
        print(2)
except KeyboardInterrupt:
    print(1)
