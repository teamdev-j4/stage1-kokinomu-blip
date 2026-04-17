import socket
import time
import threading

# make UDP socket
sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

#setup
server_address = '0.0.0.0'
server_port = 9001
print('starting up on port {}'.format(server_port))

sock.bind((server_address , server_port))

clients = {}
timeout = 10
lock = threading.Lock()

def tread_relay() :
    while True:
        print('\nwaiting to receive message')
        data, address = sock.recvfrom(4096) #receive message
        client = address

        print('receive {} bytes from {}'.format(len(data) , address))
        print(data)

        with lock :
            clients[address] = time.time()

        if data:
            with lock :
                latest_clients = clients.copy()

            for client in latest_clients.keys() :
                if client == address :
                    continue
                    
                sent = sock.sendto(data, client)

def thread_timeout() :
#session timeout
    while True :
        time.sleep(10)
        now = time.time()
        with lock :
                latest_clients = clients.copy()
        for client in latest_clients :
            if now - latest_clients[client] > timeout :
                with lock :
                    if client in clients :
                        del clients[client]

thread_relay = threading.Thread(target=tread_relay)
thread_timeout = threading.Thread(target=thread_timeout)
