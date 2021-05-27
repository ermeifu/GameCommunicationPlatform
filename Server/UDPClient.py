import socket

HOST = ''
PORT = 9999
ADDR = (HOST, PORT)

udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
