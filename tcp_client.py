import socket

# target
target_host = "www.google.com"
target_port = 80

# creating a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
