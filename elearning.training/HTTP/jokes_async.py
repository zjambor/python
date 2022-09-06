import requests
import asyncio
import aiohttp

headers = {
    'Content-Type': 'text/plan',
    'Accept': 'application/json'
}

url = "https://v2.jokeapi.dev/joke/Any"

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return response.status_code

async def main():
    while True:
        key = input('Wanna hear another joke? (yes/no)')
        if key == 'no':
            exit(0)

        joke = await fetch()

        if joke['type'] == 'twopart':
            print(joke['setup'])
            input('Press Enter')
            print(joke['delivery'])
        else:
            print(joke['joke'])

asyncio.run(main())
