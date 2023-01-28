import socket

connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(('192.168.43.45',4444))