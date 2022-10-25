import requests

url = "https://api.tfl.gov.uk/Line/bakerloo,victoria,central,jubilee,dlr"
r = requests.get(url)
assert r.status_code == 200
for line in r.json():
    name = line['name']
    mode_name = line["modeName"]
    disruptions = line["disruptions"]
    print(f"{name} [{mode_name}] {len(disruptions)} disruptions")
