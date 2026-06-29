import json

with open("network_devices.json(1)", "r") as file:
    devices = json.load(file)


print(devices[0])