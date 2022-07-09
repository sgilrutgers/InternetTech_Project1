import argparse
from sys import argv
import socket

#First we use the argparse package to parse the aruments
parser=argparse.ArgumentParser(description="""This is a very basic client program""")
parser.add_argument('-f', type=str, help='This is the source file for the strings to reverse', default='source_strings.txt',action='store', dest='in_file')
parser.add_argument('-o', type=str, help='This is the destination file for the reversed strings', default='results.txt',action='store', dest='out_file')
parser.add_argument('server_location', type=str, help='This is the domain name or ip address of the server',action='store')
parser.add_argument('port', type=int, help='This is the port to connect to the server on',action='store')
args = parser.parse_args(argv[1:])

#next we create a client socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = (args.server_location, args.port)
client_sock.connect(server_addr)

#now we need to open both files
with open(args.out_file, 'w') as write_file:
	for line in open(args.in_file, 'r'):
		#trim the line to avoid weird new line things
		line = line.strip()
		#now we write whatever the server tells us to the out_file
		client_sock.sendall(line.encode('utf-8'))
		answer = client_sock.recv(512)
		#decode answer
		answer = answer.decode('utf-8')
		write_file.write(answer + '\n')

#close the socket (note this will be visible to the other side)
client_sock.close()
