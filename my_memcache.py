import json
from pymemcache.client.base import Client


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserealizer(key, value, flags):
    if flags == 1:
        return value.decode('utf-8')
    if flags == 2:
        return  json.loads(value.decode('utf-8'))
    raise Exception('Unknown serialization format')


client = Client(('127.0.0.1', 11211), serializer=json_serializer, deserializer=json_deserealizer)
client.set('key', {'a': 'b', 'c': 'd'})
result = client.get('key')
print(result)
