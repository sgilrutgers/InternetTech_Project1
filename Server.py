import argparse
from sys import argv
import socket

#for some reason, the code is throwing a bad pipe error if we have the method below the connection to the client
#
def getIpList(data):
    #if you uncomment the return below and the print answer, it will show you that it gets returned four times
    #return ("made it")
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #this is from the given materials reading from routley.io as the DNS server is at 53
    server_addr("8.8.8.8", 53)
    #server_addr = ("www.google.com", "8.8.8.8")

    #current issue now is that the server_addr is not wanting to connect, maybe switch to sock_Dgram or treat it as client


    client_sock.connect(server_addr)
    

    while True:
        
        client_sock.sendall(data)
        answer = client_sock.recv(1024)
        if not answer:
            break
        list += answer + ","



    client_sock.close()
    return list




parser = argparse.ArgumentParser(
    description="""This is a very basic client program""")
parser.add_argument(
    'port', type=int, help='This is the port to connect to the server on', action='store')
args = parser.parse_args(argv[1:])

HOST = ''
PORT = args.port

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((HOST, PORT))
ss.listen(1)
conn, address = ss.accept()
with conn:
    while True:
        data = conn.recv(512)
        if not data:
            break
        #There is a bad pipefault occuring here
        answer = getIpList(data)
        #print(answer)

        conn.sendall(data)


