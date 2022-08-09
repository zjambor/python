import asyncio

async def set_after(fut, delay, value):
    await asyncio.sleep(delay)

    # set value as a result of 'fut' Future
    fut.set_result(value)

async def main():
    # get the current event loop
    loop = asyncio.get_running_loop()

    # create a new Future object
    fut = loop.create_future()

    # run in separate coroutine
    loop.create_task(
        set_after(fut, 1, '... world')
    )

    print("Hello, ")

    # wait until 'fut' has a result (1 sec) and print it
    print(await fut)

asyncio.run(main())
