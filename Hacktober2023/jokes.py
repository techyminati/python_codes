import requests

URL = "https://geek-jokes.sameerkumar.website/api?format=json"

res = requests.get(URL)
print(res.json()["joke"])
