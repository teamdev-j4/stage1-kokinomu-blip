import socket
import threading


sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

# setting username
username = input('Type userName : ')
username =  username.encode()
usernamelen = len(username).to_bytes(1 , "big")

# input address
server_address = input("Type in the sever's address to connect to: ")
server_port = 9001

#event for stopping tread
stop_event = threading.Event()

def recv_loop() :
    sock.settimeout(1)
    while not stop_event.is_set() :
        try :
            data, sever = sock.recvfrom(4096)
            print('{!r}'.format(data))

        except socket.timeout :
            continue

        except OSError as e:
            print(e)
            stop_event.set()

        except Exception as e:
            print(e)
            continue

    print("stopped receiving")


def send_loop() : 
    while not stop_event.is_set() :
        # input contents
        contents = input('Typing some messages : ')

        #if input 'q', stop chatting
        if contents.lower() == 'q':
            print('stopped sending message')
            stop_event.set()
            break

        print('{!r}'.format(contents))

        #sending message
        contents = contents.encode()
        message = usernamelen + username + contents
        sent = sock.sendto(message, (server_address , server_port))



thread_recv = threading.Thread(target=recv_loop)
thread_send = threading.Thread(target=send_loop)

#start tread
thread_recv.start()
thread_send.start()

thread_recv.join()
thread_send.join()

#close socket
print('closing socket')
sock.close()


