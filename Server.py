import argparse
from sys import argv
import socket


parser=argparse.ArgumentParser(description="""This is a very basic client program""")
parser.add_argument('port', type=int, help='This is the port to connect to the server on',action='store')
args = parser.parse_args(argv[1:])

HOST = ''
PORT = args.port

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind((HOST,PORT))
ss.listen(1)
conn,address = ss.accept()
with conn:
        while True:
            data = conn.recv(512)
            if not data:
                break
            data = data[::-1]
            conn.sendall(data)

def getIpList(data):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ("www.google.com", 8.8.8.8)
    client_sock.connect(server_addr)
    while True:
        client_sock.sendall(data)
        answer = client_sock.recv(1024)
        if not answer:
            break
        list += answer + ","
  
    return list
