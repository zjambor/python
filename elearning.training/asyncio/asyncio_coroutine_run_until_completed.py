import asyncio

async def corou1():
    while True:
        for _ in range(100):
            await asyncio.sleep(0.01)
        print('corou1')

async def corou2():
    for _ in range(25):
        await asyncio.sleep(0.05)
    print('corou2')

def main():
    asyncio.ensure_future(corou1())
    f = asyncio.ensure_future(corou2())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(f)
    loop.close()

if __name__ == "__main__":
    main()
