import asyncio
import contextlib
import itertools

async def client(host, port):
    reader, writer = await asyncio.open_connection(host, port)

    for i in itertools.count():
        writer.write(b'ping\n')
        response = await reader.readline()
        if i == 10000:
            return
        if response == b'pong\n':
            print(i)
        else:
            return

main = asyncio.ensure_future(client('127.0.0.1', 8899))
loop = asyncio.get_event_loop()

with contextlib.closing(loop):
    loop.run_until_complete(main)
