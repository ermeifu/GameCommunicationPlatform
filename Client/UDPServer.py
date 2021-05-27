import socket

HOST = ''
PORT = 9999
ADDR = (HOST, PORT)

udpSerSock = socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('UDP广播服务已经打开，等待广播消息...')
    break

udpSerSock.close()

