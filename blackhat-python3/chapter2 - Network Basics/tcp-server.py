# This is a TCP server implementation

import socket
import threading

# Set the IP address and port to listen on
bind_ip = "0.0.0.0"
bind_port = 9999

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server.bind((bind_ip, bind_port))

# Start listening for incoming connections
server.listen(5)

# Print a message indicating the server is listening
print("[*] Listening on %s:%d" % (bind_ip, bind_port))

# Define the function to handle each client connection
def handle_client(client_socket):
    # Receive data from the client
    request = client_socket.recv(1024)
    print("[*] Received: %s" % request.decode())
    
    # Send a response back to the client
    client_socket.send("ACK!".encode())
    client_socket.close()

# Accept and handle incoming connections
while True:
    client, addr = server.accept()
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
    
    # Start a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
