import json

data={
    'name': 'Neha',
    'age': 22,
}

print('Serializing data')
json_string = json.dumps(data, indent=2)
print(json_string)

print('Deserializing data')
json_data = json.loads(json_string)
print(json_data)