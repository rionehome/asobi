#!/usr/bin/env python

import socket

M_SIZE = 32
bind_address = ('192.168.11.45', 12345)

sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind(bind_address)

print("----- Waiting message -----")
while True:
    try :
        message, cli_addr = sock.recvfrom(M_SIZE)
        message = message.decode(encoding='utf-8')
        print("linear : {}" .format(message[0:message.find(",")]))
        print("angular: {}" .format(message[message.find(",")+1:len(message)]))

    except KeyboardInterrupt:
        print ("finish")
        sock.close()
        break