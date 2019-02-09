import socket
from ssh2.session import Session

host = 'i7mini'
user = 'hamam'
password = 'adminadmin'

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.AF_SYSTEM
sock.connect((host,22))
session = Session()
session.handshake(sock)
session.userauth_password( user, password)

channel = session.open_session()
channel.execute('ifconfig -a')
size,data = channel.read()
while size > 0 :
	print(data.decode())
	size,data = channel.read()
channel.close()