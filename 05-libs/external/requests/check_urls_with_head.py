import requests

urls = [
    "https://www.google.com/",
    "https://github.com/",
    "https://www.parcan.es/",
]

for url in urls:
    print(url, end="...", flush=True)
    r = requests.head(url)
    print(r.status_code)
