import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
plt.close("all")
#headers = ['Sensor Value','Date','Time']

df = pd.read_csv('DKA.csv',index_col=0, parse_dates=True, encoding="ISO-8859-1")

df.columns
time = (df.dtypes)
print(time)
dtemp = df["Temperature °C"]
dhumid =df["Humidity %"]
print(dtemp)
print(dhumid)

#df.plot()
#''data.A.plot()
#data.B.plot(secondary_y=True, style='g')
fig, (ax1,ax2) = plt.subplots(2,1,sharex=True)

ax1.set_ylabel('Temperature', color='b')
ax1.plot(dtemp)
ax2.set_ylabel('Humidity %', color='b')
ax2.plot(dhumid)

plt.show()



plt.show()



#data.plt()
#print(z)
#print(y)




#read.plot(read)