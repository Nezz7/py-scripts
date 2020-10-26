import yaml
import requests
import json

with open('targets.yaml') as file:
    url = yaml.load(file, Loader=yaml.FullLoader)

output = []
for target in url['targets']:
    r = requests.get(target['url'])
    cur = {}
    cur['url'] = target.get('url')
    cur['expected_status_code'] = target.get('expected_status_code')
    cur['actual_status_code'] = r.status_code
    cur['loading_time_in_seconds'] = r.elapsed.total_seconds()
    cur['success'] = cur['actual_status_code'] == cur['expected_status_code']
    output.append(cur)

print(json.dumps(output))