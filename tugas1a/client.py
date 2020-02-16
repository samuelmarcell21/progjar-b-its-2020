import sys
import socket
# import os
import errno

# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    file_name = input("Type in ur file : ")
    # my_file = os.path.join(THIS_FOLDER, file_name)
    # print(my_file)
    file = open(file_name, 'rb')
    isifile = file.read()
    sock.sendall(isifile)
    amount_received = 0
    amount_expected = len(isifile)
    while amount_received < amount_expected:
        data = sock.recv(10^24)
        print(f"data received with {len(data)} length")
        hasil = open("fromserver_"+file_name, 'a+b')
        hasil.write(data)
        amount_received += len(data)
finally:
    print (sys.stderr, 'closing socket')
    # hasil.close()
    sock.close()