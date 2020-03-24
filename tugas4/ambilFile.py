import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port_num = 8888
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1" , " Port:", port_num)
sock.connect(server_address)

try:
    namafile = "ngeteh.txt"
    msg = "get " + namafile
    print ("Requesting File to Server")
    sock.send(msg.encode())

    isifile = sock.recv(4096)
    tmp = open(namafile,"wb")
    tmp.write(isifile)
    tmp.close()
    
    print("File has been Received")
finally:
    print("Closing Connection")
    sock.close()