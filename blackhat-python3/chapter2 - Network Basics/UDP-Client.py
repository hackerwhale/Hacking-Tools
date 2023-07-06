# Import the socket module
import socket

# Define the target host and port
target_host = "127.0.0.1"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data to the target host and port
client.sendto("AAABBBCCC".encode(), (target_host, target_port))

# Receive some data from the target host
data, addr = client.recvfrom(4096)

# Print the received data after decoding it from bytes to string
print(data.decode())
