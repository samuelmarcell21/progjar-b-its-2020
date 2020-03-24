import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port_num = 8888
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1" , " Port:", port_num)
sock.connect(server_address)

try:
    msg = "list"
    sock.send(msg.encode())
    print("Requesting list of file")
    data = sock.recv(2048)
    print("List of File accepted!")
    print(data.decode())
finally:
    sock.close()