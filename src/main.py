import json

with open("data/calls.json") as f:
    calls = json.load(f)

print(calls)
