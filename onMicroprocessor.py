import machine
import time
import urequests
import network
import dht

# Connect to Wi-Fi
ssid = "your_network_name"
password = "your_network_password"
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    time.sleep(1)
print("Connected to Wi-Fi")

# Read sensor data
adc = machine.ADC(26)
gas = adc.read_u16()
print("Gas concentration:", gas)

d = dht.DHT11(machine.Pin(16))
d.measure()
temp = d.temperature()
hum = d.humidity()
print("Temperature:", temp)
print("Humidity:", hum)

# Send HTTP POST request to computer
url = "http://your_computer_ip_address:5000/data"
data = {"gas_concentration": gas, "temperature": temp, "humidity": hum}
headers = {"Content-Type": "application/json"}
response = urequests.post(url, json=data, headers=headers)
print(response.text)
