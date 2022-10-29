import socket
import matplotlib.pyplot as plt

HOST = '140.112.211.102' # IP address
PORT = 6969 # Port to listen on (use ports > 1023)
t, h, p, mx, my, mz, gx, gy, gz, x, y, z, number = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("Connected at", addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print(f"Received from socket server:{data}")
            if data == '': break

            data = data.split(' ')
            t.append(float(data[0]))
            h.append(float(data[1]))
            p.append(float(data[2]))
            mx.append(float(data[3]))
            my.append(float(data[4]))
            mz.append(float(data[5]))
            gx.append(float(data[6]))
            gy.append(float(data[7]))
            gz.append(float(data[8]))
            x.append(float(data[9]))
            y.append(float(data[10]))
            z.append(float(data[11]))
            number.append(float(data[12]))
            plt.pause(0.0001)

fig = plt.figure()
temp = fig.add_subplot(2, 3, 1)
hum = fig.add_subplot(2, 3, 2)
press = fig.add_subplot(2, 3, 3)
mag = fig.add_subplot(2, 3, 4, projection='3d')
gyro = fig.add_subplot(2, 3, 5, projection='3d')
acce = fig.add_subplot(2, 3, 6, projection='3d')           
temp.plot(number, t)
temp.set_xlabel("Data number", fontsize=16)
temp.set_ylabel("Temperature ($^\circ$C)", fontsize=16)
hum.plot(number, h)
hum.set_xlabel("Data number", fontsize=16)
hum.set_ylabel("Humidity (%%)", fontsize=16)
press.plot(number, p)
press.set_xlabel("Data number", fontsize=16)
press.set_ylabel("Pressure (mBar)", fontsize=16)
mag.plot(mx, my, mz)
mag.set_xlabel('x', fontsize=16, rotation=150)
mag.set_ylabel('y', fontsize=16)
mag.set_zlabel('z', fontsize=16)
mag.set_title("Magnetometer", fontsize=20)
gyro.plot(gx, gy, gz)
gyro.set_xlabel('x', fontsize=16, rotation=150)
gyro.set_ylabel('y', fontsize=16)
gyro.set_zlabel('z', fontsize=16)
gyro.set_title("Gyroscope", fontsize=20)
acce.plot(x, y, z)
acce.set_xlabel('x', fontsize=16, rotation=150)
acce.set_ylabel('y', fontsize=16)
acce.set_zlabel('z', fontsize=16)
acce.set_title("Accelerator", fontsize=20)
fig.tight_layout(pad=1.5)
plt.show()
