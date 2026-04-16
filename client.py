import socket

sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

# setting username
username = input('Type userName : ')
username =  username.encode()
usernamelen = len(username).to_bytes(1 , "big")

# input address
server_address = input("Type in the sever's addressn to connect to: ")
server_port = 9001

# input contents
contents = input('Typing some messages : ')
contents = contents.encode()

message = usernamelen + username + contents
messagelen = len(message)
if messagelen > 4096 :
    print()

try :
    print('sending {!r}'.format(message))

    sent = sock.sendto(message, (server_address , server_port))
    print('send {} byte'.format(sent))

    print('waiting to receive')
    data, sever = sock.recvfrom(4096)
    print('receive {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()