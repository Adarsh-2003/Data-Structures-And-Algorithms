import json

with open("new.json", "w"):
    x = {
  "name": "Adarsh",
  "age": 22,
  "city": "Mumbai"
    }
    json.dumps(x)

print("done")