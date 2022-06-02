#!/usr/bin/env python

import socket
import pygame
from pygame.locals import *

M_SIZE = 32
serv_address = ('192.168.11.45', 12345)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pygame.joystick.init()
try:
   joystick = pygame.joystick.Joystick(0)
   joystick.init()
except pygame.error:
   print("not found joystick")
pygame.init()

print("Ready to send")
print("----- Send messages -----")
while True:
    try:
        for e in pygame.event.get():
            if e.type == pygame.locals.JOYAXISMOTION:
                linear = round(joystick.get_axis(1), 3)
                angular = round(joystick.get_axis(2), 3)
                message = str(linear) + "," + str(angular)
                send_len = sock.sendto(message.encode('utf-8'), serv_address)
                print(message)

    except KeyboardInterrupt:
        print("----- finish -----")
        sock.close()
        break
