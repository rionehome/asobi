#!/usr/bin/env python

import socket

M_SIZE = 32

serv_address = ('192.168.11.45', 12345)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


print("Ready to send")
print("----- Send messages -----")
while True:
    try:
        message = "123,456"
        send_len = sock.sendto(message.encode('utf-8'), serv_address)

    except KeyboardInterrupt:
        print("----- finish -----")
        sock.close()
        break