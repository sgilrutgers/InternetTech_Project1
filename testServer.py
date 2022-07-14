import socket
import binascii


def format_hex(hex):
    """format_hex returns a pretty version of a hex string"""
    octets = [hex[i:i+2] for i in range(0, len(hex), 2)]
    pairs = [" ".join(octets[i:i+2]) for i in range(0, len(octets), 2)]
    return "\n".join(pairs)

def getIp(msg):
    list = str(int(msg[0],16)) +"."+str(int(msg[1],16)) +"."+str(int(msg[2],16)) +"."+str(int(msg[3],16))
    print(list)
    return list
def getIpList(packetLen, msg):
    startIndex = int((packetLen +24)/2);
    msg = msg.replace("\n"," ")
    # print(msg)
    msg = msg.split(" ")
    msglen = len(msg)
    #print(msg)
    ipList = ""
    for x in range(startIndex, msglen):
        if(msg[x] == "c0"):
            if((x+11)<msglen):
                if(msg[x+11] == "04"):
                    ip = [msg[x+12],msg[x+13],msg[x+14],msg[x+15]]
                    ipList += getIp(ip) +","
                    #print(msg[x+12]+" "+ msg[x+13]+" "+ msg[x+14]+" "+ msg[x+15])
    return ipList

message = "www.facebook.com"
msgList= message.split('.')
res = "AA AA 01 00 00 01 00 00 00 00 00 00"
for x in msgList:
    lent = len(x)
    if(lent<10):
        strlen = "0"+str(lent)
    else:
        strlen = str(lent)
    res += " " + strlen
    for y in x:
        res += " " + binascii.hexlify(y.encode("utf-8")).decode("utf-8")
res += " " + "00 00 01 00 01"
packetLen = len((res.replace(" ", "")))

print(res)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.connect(('8.8.8.8', 53))

res = res.replace(" ", "").replace("\n", "")
strmsg = binascii.unhexlify(res)
print(strmsg)

client_sock.sendto(strmsg,('8.8.8.8',53) )
data, addr= client_sock.recvfrom(4096)
client_sock.close()

data = binascii.hexlify(data).decode("utf-8")
datalist = format_hex(data)
#print(datalist)
print(getIpList(packetLen,datalist))
