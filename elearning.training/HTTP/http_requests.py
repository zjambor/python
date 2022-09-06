import requests

payload = {
    "name": "Tamas"
}
headers = {
    'Content-Type': 'text/plan',
    'Accept': 'application/json'
}

def print_answer(r):
    if r.ok:
        print(f"response.status_code: {r.status_code}")
        print(f"response.ok: {r.ok}")
        print(f"response.headers: {r.headers}")
        print(f"response.url: {r.url}")
        print(f"response.cookies: {r.cookies}")
        print(f"response.raw: {r.raw}")
        print("Text:\n", r.text)
        print("Content:\n", r.content)
        print("json:\n", r.json())
    else:
        print(f"Error occured while sending request {r.status_code}")

url = "https://httpbin.org/get"
r = requests.get(url, headers=headers, data=payload)
print_answer(r)

# Error
url = "https://httpbin.org/status/404"
r = requests.get(url, headers=headers, data=payload)
print_answer(r)

# Sessions
url = "https://httpbin.org/get"
with requests.Session() as s:
    print("*" * 50)
    req = requests.Request("GET", url, headers=headers, data=payload).prepare()
    r = s.send(req)
    print_answer(r)

# Cookies
url = "https://httpbin.org/cookies/set/name/value"
r = requests.get(url, headers=headers, data=payload)
print_answer(r)
