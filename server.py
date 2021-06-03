import socket
import threading

#MESSAGE LENGTH
HEADER= 64
#decoding message from byte to string
FORMAT='utf-8'
#connecting port usually choose free one
PORT= 5050
#server ip address
SERVER="192.168.0.11"
#gets server IP address for any computer
SERVER= socket.gethostbyname(socket.gethostname())

#binding the socket and port
ADDR = (SERVER, PORT)

#disconnect message
DISCONNECT_MESSAGE = "!DISCONNECT"


#make socket TYPES OF socket that can join to the server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected.")

    connected = True
    while connected:
        msg_length= conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length= int(msg_length)
            msg= conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}]{msg}")
            conn.send("msg received".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[Listening] server is listening on {SERVER}")
    while  True:
        conn, addr = server.accept()
        thread= threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active connection] {threading.activeCount() -1 }")

print("Server is starting")
start()


