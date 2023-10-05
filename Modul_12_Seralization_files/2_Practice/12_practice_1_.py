import pickle

data = ['1', 345, 'Hello']

serialize_data = pickle.dumps(data)
deserialize_data = pickle.loads(serialize_data)

print(deserialize_data is data)
print(deserialize_data == data)
