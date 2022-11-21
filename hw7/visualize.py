import matplotlib.pyplot as plt

num = []
for i in range(320):
    num.append(i)
# Insert the output from the Mbed Studio terminal 
acc_sensor_input = []
filter_output = []

plt.plot(num, acc_sensor_input, 'b', label='Sensor input values')
plt.plot(num, filter_output, 'r', label='Filter output values')
plt.title(label='Accelerometer X values')
plt.legend()
plt.show()
