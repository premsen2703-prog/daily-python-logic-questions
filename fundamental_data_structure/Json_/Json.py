import json

# Python Dictionary to JSON String (Serialization)
user_data = {"name": "Alice", "age": 25, "is_admin": False}
json_string = json.dumps(user_data, indent=5)

# JSON String back to Python Dictionary (Deserialization)
parsed_dict = json.loads(json_string)
print(json_string)
print(parsed_dict)