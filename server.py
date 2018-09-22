import socket
import sys

def socket_create():
	try:
		global host
		global port
		global s

		host = 'localhost'
		port = 9999  # identify data coming in. Use uncommon port number
		s = socket.socket()
	except socket.error as error:
		print ("socket creation error: " + str(error))

# binding socket to port
def socket_bind():
	try:
		global host
		global port
		global s

		print("binding socket to port: " + str(port))
		s.bind((host,port)) #host could be ip address. Here same machine are used so no ip
		s.listen(5)
	except socket.error as msg:
		print("socket binding error: " + str(msg) + "\n" + "Retrying...")
		socket_bind()

# establishing a connection iif socket is listening
def socket_accept():
	conn, address = s.accept()
	print("Connection has been established : IP address :" + address[0] + ": Port : " + str(address[1]))
	send_commands(conn)
	conn.close()

def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			s.close()
			sys.exit()

		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), "utf-8") 
			#converting to string because recieved info is in bytes.
			#1024 is buffer size
			print(client_response, end = "")

def main():
	socket_create()
	socket_bind()
	socket_accept()

main()

