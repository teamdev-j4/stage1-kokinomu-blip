import socket
import time

# make UDP socket
sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 9001
print('starting up on port {}'.format(server_port))

socket.bind((server_address , server_port))

clients = {}
timeout = 10

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    client = address

    now = time.time()

    print('receive {} bytes from {}'.format(len(data) , address))
    print(data)

    clients[address] = time.time()

    if data:
        for i in list(clients.keys()) :
            if client == address :
                continue
                
            sent = sock.sendto(data, client)

    #session timeout
    while True :
        time.sleep(10)
        for client in list(clients.key()) :
            if now - clients[client] > timeout :
                del clients[client]
        