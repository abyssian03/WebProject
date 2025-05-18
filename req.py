import requests


r = requests.get("https://github.com/", auth=("jannynovosib", "big0blob0bubble"))
if r.status_code == 200:
    print("OK")
