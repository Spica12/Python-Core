import json

data = {1: [1, 2, 3, 4, 5],
        'tuple': ('a', 'b', 'c')
}

with open('data.json', 'w') as fh:
    json.dump(data, fh)

s_json = json.dumps(data)
d_json = json.loads(s_json)

print(d_json is data)
print(d_json == data)