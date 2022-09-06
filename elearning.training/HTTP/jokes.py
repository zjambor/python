import requests

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

# def print_answer(r):
#     if r.ok:
#         # if r.type == "single":
#         #     print(r.joke)
#     else:
#         print(f"Error occured while sending request {r.status_code}")

url = "https://v2.jokeapi.dev/joke/Any"
r = requests.get(url)
print_answer(r)
