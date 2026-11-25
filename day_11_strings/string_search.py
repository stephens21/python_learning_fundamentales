device_name = "NETWORK_ROUTER_01"

if "ROUTER" in device_name:
    print("FOUND")
else:
    print("NOT FOUND")

position = device_name.find("ROUTER")
print(position)

device_name_new = device_name.replace("_", "-")
print(device_name_new)
if device_name.startswith("NETWORK"):
    print("SUCCESS")
else:
    print("FAILURE")