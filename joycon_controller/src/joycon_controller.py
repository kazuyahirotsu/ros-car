#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import pygame
from pygame.locals import *
import time

class joyconController:
    def __init__(self):
        rospy.init_node('joycon_node', anonymous=True)
        self.twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1000)
        
        pygame.joystick.init()
        self.joystick0 = pygame.joystick.Joystick(0)
        self.joystick0.init()
        pygame.init()


        self.linearx = 0
        self.angularz = 0

        twist = Twist()
        self.twist_pub.publish(twist)

        rospy.Timer(rospy.Duration(0.1), self.timerCallback)
    def timerCallback(self, event):
        twist = Twist()
        eventlist = pygame.event.get()


        for e in eventlist:
            if e.type == QUIT:
                return

            elif e.type == pygame.locals.JOYBUTTONDOWN:
                if e.button==2:
                    self.linearx -= 0.1
                elif e.button==1:
                    self.linearx += 0.1
                elif e.button==0:
                    self.angularz += 0.1
                elif e.button==3:
                    self.angularz -= 0.1
                print('linear x:' + '{:.1f}'.format(self.linearx) + ', angular z:' + '{:.1f}'.format(self.angularz))

        twist.linear.x  = self.linearx
        twist.angular.z = self.angularz

        self.twist_pub.publish(twist)

if __name__ == '__main__':
    jc = joyconController()
    rospy.spin()