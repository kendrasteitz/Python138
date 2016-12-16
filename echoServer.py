import socket
import sys

host = "192.168.1.106"
port = 8989
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket Created")

try:
    s.bind((host, port))

except socket.error as msg:

    print("Connection failed. Error Code: " + str(msg[0]) + " Message " + msg[1])
    sys.exit()

print("Socket connection complete")
s.listen(5)
print("Socket now listening")

while 1:
    connection, address = s.accept()
    print("Connected with" + address[0] + ":" + str(address[1]))

s.close()



