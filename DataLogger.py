import requests
from datetime import datetime
import csv
import time


#Connecting to server
link = "http://192.168.0.33"

#Create header
header = ['Time','Temperature °C', 'Humidity %','pTemperature °C', 'pressure', 'Lux', 'Moisture Sensor']

# Definition CSV writer mit header
def write_csv(data, header):
        with open('Schimmel2311.csv','a', newline='') as outfile:
            writer = csv.writer(outfile)
            if outfile.tell() == 0:
                writer.writerow(header)
            writer.writerow(data)

#header_csv(header)
#Loop to log data and save it to csv
while True:
    try:
        f = requests.get(link)
        data = f.json()
        temperature = data['temperature']
        humidity = data['humidity']
        ptemperature = data['ptemperature']
        pressure = data['pressure']
        lux = data['Lux']
        moist = data['moist']

        now = datetime.now()
        now = str(now)
        sensor_data = [now,temperature,humidity,ptemperature,pressure, lux, moist]
        write_csv(sensor_data, header)
        print(sensor_data)
        time.sleep(5)
    except:
        pass








