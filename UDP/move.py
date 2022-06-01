#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import socket

if __name__ == '__main__':
    rospy.init_node('move_operation')
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size = 1)
    t = Twist()

    M_SIZE = 32
    bind_address = ('192.168.11.45', 12345)

    sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.bind(bind_address)

    print("----- Waiting message -----")
    while True:
        try :
            message, cli_addr = sock.recvfrom(M_SIZE)
            message = message.decode(encoding='utf-8')
            linear = float(message[0:message.find(",")])
            angular = float(message[message.find(",")+1:len(message)])
            t.linear.x = (-1) * linear / 10
            t.angular.z = (-1) * angular / 2
            pub.publish(t)
            print("linear : {}" .format(linear))
            print("angular: {}" .format(angular))

        except KeyboardInterrupt:
            print ("----- finish -----")
            sock.close()
            break

