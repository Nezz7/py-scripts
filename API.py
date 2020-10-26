import requests
import json

r = requests.get('https://api.spacexdata.com/v3/launches')
response = r.json()

for mission in response:
    cur_sum = 0
    for payload in mission['rocket']['second_stage']['payloads']:
        if payload['payload_mass_kg'] is not None :
            cur_sum = cur_sum + int(payload['payload_mass_kg'])
    if cur_sum >= 800 :
        print(mission["mission_name"])
