import sys
import socket
import errno
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print (sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from', client_address)
    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(10000)
        print (f'received {len(data)}')
        # print (f'sending {thalut}')
        if data:
            print ('sending data back to the client')
            connection.sendall(data)
        else:
            print (sys.stderr, 'no more data from', client_address)
            break 
    # Clean up the connection
    connection.close()