import socket

# target
target_host = "www.google.com"
target_port = 80

# creating a socket object
# AF_INET refers to the ipv4 address family
# SOCK_STREAM indicates TCP socket type
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting our client
client.connect((target_host, target_port))

# send data
# this is an HTTP GET request, (requesting data from server) 
# from the root (/) directory
client.send((b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"))

# receive the server's response (up to 4096 bytes)
response = client.recv(4096)

# decode raw bytes into readable format
print(response.decode())

# close our client
client.close()