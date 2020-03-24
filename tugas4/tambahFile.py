import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port_num = 8888
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1" , " Port:", port_num)
sock.connect(server_address)

try:
    namafile = "cobacoba.txt"
    tmp = open(namafile,"rb")
    file = tmp.read(4096)
    tmp.close()
    file = file.decode()
    msg = "add " + namafile + " " + file
    print(msg)
    print (f"Adding {namafile}")
    sock.send(msg.encode())
    message = sock.recv(4096).decode()
    print(message)
finally:
    print("Closing Connection")
    sock.close()