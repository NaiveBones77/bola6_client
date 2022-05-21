import socket
import numpy as np
import matplotlib.pyplot as plt
import utils

localIP = "127.0.0.1"
localPort = 12346
bufferSize = 1024

dict1 = {'1':None, '2':None}

plt.ion()

r = np.arange(0, 2, 0.01)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
plt.autoscale(False)
#line1, = ax.plot(0, 0)
# Установить направление полярной оси
ax.set_theta_zero_location("N")
# задаем направление по часовой стрелке
ax.set_theta_direction(-1)
# отображение линии сетки полярного диаметра
ax.set_rticks([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]) # Less radial ticks
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


    dict1 = utils.checkS(message, dict1)

    if (None in dict1.values()):
        pass
    else:
        x, y = utils.formList(dict1)
        scat = plt.scatter(np.arctan2(y, x), np.sqrt(np.power(x, 2) + np.power(y, 2)))
        plt.draw()
        plt.pause(0.5)
        scat.remove()


    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

