import json

data1 = {'b': 789, 'c': 456, 'a': 123}
encode_json = json.dumps(data1)
print type(encode_json), encode_json

decode_json = json.loads(encode_json)
print type(decode_json)
print decode_json['a']
print decode_json