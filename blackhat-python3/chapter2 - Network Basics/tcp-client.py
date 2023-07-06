# Import the socket module
import socket

# Define the target host and port
target_host = "www.google.com"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to the target host and port
client.connect((target_host, target_port))

# Prepare the HTTP GET request
request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_host)

# Send the request to the server after encoding it as bytes
client.send(request.encode())

# Receive the response from the server
response = client.recv(4096)

# Print the response after decoding it from bytes to a string
print(response.decode())
