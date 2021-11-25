import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
plt.close("all")
##headers = ['Sensor Value','Date','Time']

df = pd.read_csv('Schimmel2311.csv',index_col=0, parse_dates=True, encoding="ISO-8859-1")

df.columns
time = (df.dtypes)

dh = df["Humidity %"]
dt1 = df["Temperature °C"]
dp = df["pressure"]
dt2 = df["pTemperature °C"]
lux = df["Lux"]
soil = df["Moisture Sensor"]

fig1, (ax1,ax2,ax3) = plt.subplots(3,1,sharex=True)
fig2, (ax4,ax5) = plt.subplots(2,1,sharex=True)
# fig, ax = plt.subplots(2,2,sharex=True)

ax1.set_ylabel('Temperature', color='b')
ax1.plot(dt1)
ax1.plot(dt2)
ax2.set_ylabel('Humidity %', color='b')
ax2.plot(dh)
ax3.set_ylabel('Pressure', color='b')
ax3.plot(dp)
ax4.set_ylabel('Lux', color='b')
ax4.plot(lux)
ax5.set_ylabel('Moisture Sensor', color='b')
ax5.plot(soil)



plt.show()


#Hausaufgabe for-Schleife :)
# for
# ax[1][0].set_ylabel('Temperature', color='b')
# ax[1][0].plot(dt1)