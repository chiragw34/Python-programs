import socket

host = 'localhost'
port = 6766

s = socket.socket()
s.connect((host, port))

str = input("He: ")
while str != 'exit':
	s.send(str.encode())
	
	data = s.recv(1024)
	data = data.decode()
	print("She: " + data)
	
	str = input("He: ")

s.close()