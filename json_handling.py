import json

# some JSON:
json_data = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
dict_data = json.loads(json_data)

# the result is a Python dictionary:
print(dict_data["age"])
print(dict_data["name"])

#============================================
print("***** CONVERTINT DICTIONARY DATA TO JSON DATA ******")
# a Python object (dict):
dict_data2 = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
json_data2 = json.dumps(dict_data2)

# the result is a JSON string:
print(json_data2)
