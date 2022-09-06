import requests

headers = {
    'Content-Type': 'text/plan',
    'Accept': 'application/json'
}

url = "https://v2.jokeapi.dev/joke/Any"

while True:
    key = input('Wanna hear another joke? (yes/no)')
    if key == 'no':
        break
    # response = requests.request("GET", url, headers=headers)
    response = requests.get(url, headers=headers)
    joke = response.json()

    if joke['type'] == 'twopart':
        print(joke['setup'])
        input('Press Enter')
        print(joke['delivery'])
    else:
        print(joke['joke'])
