import json
import collections
file = open('log.txt', 'r')
json_data = []

for line in file:
    json_line = json.loads(line)
    json_data.append(json_line)

methods = []
for cur in json_data:
    methods.append(cur['method'])

occurrences_methods = collections.Counter(methods)
sorted_methods = occurrences_methods.most_common()

for http_request, occ in sorted_methods :
    print(occ,' ', http_request)
