import socket
import datetime

# Set the IP and port to listen on
ip = '0.0.0.0'
port = 22

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and port
sock.bind((ip, port))

# Listen for incoming connections
sock.listen(1)

print(f'Honeypot listening on {ip}:{port}')

while True:
    # Accept a connection
    conn, addr = sock.accept()
    print(f'Connection from {addr}')
    
    # Receive data from the connection
    data = conn.recv(1024)
    
    # Log the attempt
    with open('honeypot.log', 'a') as f:
        f.write(f'{datetime.datetime.now()} - {addr[0]}:{addr[1]} - {data.decode()}\n')
    
    # Close the connection
    conn.close()