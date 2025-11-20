from netmiko import ConnectHandler
import json

with open('configs.json', 'r') as file:
   device_config2 = json.load(file)

loop200_ip = device_config2['config2']['loop200']
loop200_mask = device_config2['config2']['mask']

## Device Information
FW = {
   'device_type': 'cisco_ios_telnet',
   'host': '192.168.102.11',
   'port': 23,
   'username': 'admin',
   'password': 'pass',
   'secret': 'pass',
   #'key': [1,2,'three']
}

#print(FW['key'][2])

#device config
configs = [
   'int lo100',
   'ip add 100.100.100.100 255.255.255.255',
   'end'
]

config2 = [
   'int lo200',
   f'ip add {loop200_ip} {loop200_mask}',
   'end'
]

## connect to the device
access_cli = ConnectHandler(**FW)
access_cli.enable()
output = access_cli.send_config_set(config2)
access_cli.disconnect()

print(output)
