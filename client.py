import socket
import numpy as np
import matplotlib.pyplot as plt

localIP = "127.0.0.1"
localPort = 12346
bufferSize = 1024

r = np.arange(0, 2, 0.01)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
#plt.ion()
# Установить направление полярной оси
ax.set_theta_zero_location("N")
# задаем направление по часовой стрелке
ax.set_theta_direction(-1)
# отображение линии сетки полярного диаметра
ax.set_rticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]) # Less radial ticks
ax.set_rlabel_position(-22.5) # Move radial labels away from plotted line

ax.grid(True)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
# Listen for incoming datagrams
while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    message = message.decode("utf-8")

    a = message.replace(",", ".").split(" ")
    x = float(a[0])
    h = float(a[1])
    y = float(a[2])

    coor = [x, y]

    #scat = plt.scatter(x, y)
    #plt.draw()
    #plt.pause(2)
    #scat.remove()

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(coor)