import serial
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configure the serial port and baud rate according to your setup
ser = serial.Serial('COM9', 9600)
time.sleep(2)

data = []

def update(frame):
    line = ser.readline().decode('utf-8').strip()
    if line:
        voltage = float(line)
        data.append(voltage)
        
        plt.cla()
        plt.plot(data, label='Voltage (V)')
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.legend(loc='upper right')
        plt.tight_layout()

ani = FuncAnimation(plt.gcf(), update, interval=1000)

plt.show()

# Export data to Excel after stopping the plot
df = pd.DataFrame(data, columns=['Voltage'])
df.to_excel('voltage_data_2normal_dinh.xlsx', index=False)
