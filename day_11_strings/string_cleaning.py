device_name = "   router-01   "
device_type = "network equipment"
device_brand = "CISCO"

clean_space = device_name.strip()
upper_name =  device_name.upper()
capitalize_type = device_type.title()
lower_name = device_brand.lower()

print(f'DEVICE NAME:{upper_name}')
print(f'DEVICE TYPE:{capitalize_type}')
print(f'BRAND:{lower_name}')