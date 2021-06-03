import socket

#MESSAGE LENGTH
HEADER= 64
#decoding message from byte to string
FORMAT='utf-8'
#connecting port usually choose free one
PORT= 5050

#server is different from server side
SERVER= socket.gethostbyname(socket.gethostname())

#binding the socket and port
ADDR = (SERVER, PORT)

#SOCEKT FOR THE CLIENT
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
#disconnect message
DISCONNECT_MESSAGE = "!DISCONNECT"

def send(msg):
    message = msg.encode(FORMAT)
    msg_length= len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER- len(send_length))
    client.send(send_length)
    client.send(message)
    #print msg from server
    print(client.recv(2048).decode(FORMAT))
send("hello world")
send("hello how are you?")
send (DISCONNECT_MESSAGE)


