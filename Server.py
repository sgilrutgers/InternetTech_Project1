import socket
import binascii
import argparse
from sys import argv


def format_hex(hex):
    """format_hex returns a pretty version of a hex string"""
    octets = [hex[i:i+2] for i in range(0, len(hex), 2)]
    pairs = [" ".join(octets[i:i+2]) for i in range(0, len(octets), 2)]
    return "\n".join(pairs)

def getIp(msg):
    ip1=int(msg[0],16)
    ip2= int(msg[1],16)
    ip3 = int(msg[2],16)
    ip4 = int(msg[3],16)
    finalIp = ""       #Also had to initialized it first

    if(ip1 > 0 and ip1 < 255):
        if(ip2 < 255 and  ip2>= 0):
            if(ip3 < 255 and ip3>= 0):
                if(ip4 < 255 and ip4 >= 0):
                    finalIp = str(ip1) +"."+str(ip2) +"."+str(ip3) +"."+str(ip4)
    return finalIp

def getIpList(packetLen, msg):
    msg = msg.replace("\n"," ")
    msg = msg.split(" ")
    msglen = len(msg)

    ipList = ""
    if(msg[3] == "01"):
        return("NXDOMAIN")


    for x in range(msglen):

        if(msg[x] == "c0"):

            if((x+11)<msglen):

                if(msg[x+11] == "04"):

                    ip = [msg[x+12],msg[x+13],msg[x+14],msg[x+15]]
                    ipList += getIp(ip) +","
    return ipList

#splices code into readable format
def spliceCode(message):
    msgList= message.split('.')
    res = "AA AA 01 00 00 01 00 00 00 00 00 00"

    for x in msgList:
        lent = len(x)
        hexlen = hex(lent) # turning int length into hex
        strlen = str(hexlen) # hex into string
        strlen = strlen.replace("0x","") # removing the inital "0xAA" to just have "AA"

        if(len(strlen) == 1):  # if its just "A" then adding "0" to make "0A"
            strlen ="0" +strlen

        res += " " + strlen

        for y in x:
            res += " " + binascii.hexlify(y.encode("utf-8")).decode("utf-8")

    res += " " + "00 00 01 00 01"
    packetLen = len((res.replace(" ", "")))
    res = res.replace(" ", "").replace("\n", "")
    strmsg = binascii.unhexlify(res)

    return connectDNS(strmsg, packetLen)



def connectDNS(msg, packetLen):

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.connect(('8.8.8.8', 53))
    client_sock.sendto(msg,('8.8.8.8',53))
    data, addr= client_sock.recvfrom(4096)
    data = binascii.hexlify(data).decode('utf-8')

    datalist = format_hex(data)
    client_sock.close()

    return(getIpList(packetLen,datalist))




parser = argparse.ArgumentParser(description="""This is a very basic client program""")
parser.add_argument('port', type=int, help='This is the port to connect to the server on', action='store')
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
        list = spliceCode(data.decode('utf-8'))
        conn.sendall(list.encode('utf-8'))
