import asyncio
import aiohttp
import random

async def fetch(delay=5):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://httpbin.org/delay/{delay}') as response:
            if response.status == 200:
                return await response.json()
            else:
                return response.status_code

async def main():
    tasks = []
    for _ in range(5):
        task = asyncio.ensure_future(fetch(random.randint(1, 5)))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)

    print(responses)

asyncio.run(main())
