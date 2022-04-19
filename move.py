#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time
import socket

class Movement():
    def __init__(self):
        self.pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size = 1)
        self.move_on = 0

    def move(self):
        target_time = 8

        t = Twist()
        t.linear.x = (-1) * self.move_on * 0.2
        t.angular.z = 0

        start_time = time.time()
        end_time = time.time()

        rate = rospy.Rate(50)
        
        while end_time - start_time <= target_time:
            self.pub.publish(t)
            end_time = time.time()
            rate.sleep()

    def sub(self, data):
        if data == 0:
            self.move_on = 0.5
        elif data == 1:
            self.move_on = -0.5
        else:
            self.move_on = 0
        
        self.move()

if __name__ == '__main__':
    rospy.init_node('move_operation')
    movement = Movement()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.11.45', 12345))
    s.listen(5)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        print("accept...")
        conn, addr = s.accept()
        data = conn.recv(1024)
        print("data: {}, addr: {}" .format(data, addr))
        conn.sendall(b"Received: " + data)
        movement.sub(int(data))

        rate.sleep()

    s.close()
