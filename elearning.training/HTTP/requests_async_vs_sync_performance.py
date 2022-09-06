import asyncio
import aiohttp
import requests
import random
import time

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://httpbin.org/get') as r:
            if r.status == 200:
                return await r.json()
            else:
                return r.status_code

def fetch_sync(session):
        r = session.get(f'http://httpbin.org/get')
        if r.ok:
            return r.json()
        else:
            return r.status_code

async def main(num_requests):
    start = time.time()
    tasks = []
    for _ in range(num_requests):
        task = asyncio.ensure_future(fetch())
        tasks.append(task)

    await asyncio.gather(*tasks)
    end = time.time()
    print(f'async took {end - start}')

async def main_sync(num_requests):
    start = time.time()
    with requests.Session() as s:
        for _ in range(num_requests):
            fetch_sync(s)
    end = time.time()
    print(f'sync took {end - start}')

main_sync(50)
asyncio.run(main(50))
