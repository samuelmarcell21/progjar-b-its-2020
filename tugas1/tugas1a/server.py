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
        print(f"data received with {len(data)} length")
        hasil = open("dariserver" + ".jpg", 'a+b')
        if not data:
            hasil.close()
            break
        hasil.write(data)
        # print (f'sending {thalut}')
    # Clean up the connection
    connection.close()