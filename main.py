import json
import requests
import numpy as np
from datetime import datetime
import csv
import time
import pandas as pd

#Connecting to server
link = "http://192.168.0.33"
f = requests.get(link)
data = f.json()
print(data)


#Json kommt weg
Temperature = int(data['temperature'])
print(Temperature)

Humidity = int(data['humidity'])
print(Humidity)

#Determine time
now = datetime.now()
now = str(now)


#Create Sensor_data
header = ['Time','Temperature °C', 'Humidity %']
sensor_data = [now,Temperature,Humidity]
print(sensor_data)

# Definition CSV writer
def write_csv(data):
    with open('sensor.csv','a', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)

#sensoren abfragen und in array saven
while True:
    f = requests.get(link)
    data = f.json()
    Temperature = int(data['temperature'])
    Humidity = int(data['humidity'])
    now = datetime.now()
    now = str(now)
    sensor_data = [now,Temperature,Humidity]
    write_csv(sensor_data)
    print(sensor_data)
    time.sleep(10)

#writer.writerow(header)




#write_csv(sensor_data)
#time.sleep(10)
#write_csv(sensor_data)
#sleep(10)


