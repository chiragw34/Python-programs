import socket

host = 'localhost'
port = 6766

s = socket.socket()
s.bind((host, port))
s.listen(1)
c, address = s.accept()
print("Client connected")

while True:
	data = c.recv(1024)
	
	if not data:
		break
	print("He: " + str(data.decode()))
	datab = input("She: ")
	c.send(datab.encode())
	
s.close()