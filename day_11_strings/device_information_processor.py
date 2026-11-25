raw_data = "   router-01,192.168.1.1,ROUTER,CISCO   "

raw_data_strip = raw_data.strip()
print(raw_data_strip)

raw_data_split = raw_data_strip.split(',')

for i in range(len(raw_data_split)):
    raw_data_split[i] = raw_data_split[i].strip()

device_name = raw_data_split[0].upper()
device_ip = raw_data_split[1]
device_type = raw_data_split[2].upper()
device_brand = raw_data_split[3].title()

device = {}

device['name'] = device_name
device['ip'] = device_ip
device['type'] = device_type
device['brand'] = device_brand

print("\n================================")
print("DEVICE INFORMATION REPORT")
print("================================")
print(f'DEVICE NAME:{device['name']}')
print(f'DEVICE IP:{device['ip']}')
print(f'DEVICE TYPE:{device['type']}')
print(f'BRAND:{device['brand']}')