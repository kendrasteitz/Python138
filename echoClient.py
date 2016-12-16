import socket

host = "192.168.1.106"
port = 23455
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

s.connect((host, port))

#s.listen(5)
#print("Socket now listening")

#msg = input("Enter something: ")
s.sendall(b'Hello, world')
data = s.recv(1024)

s.close()
print('Received', repr(data))
