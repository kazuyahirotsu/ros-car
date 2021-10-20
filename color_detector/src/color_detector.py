#!/usr/bin/env python

import numpy as np
import rospy
import cv2
from cv_bridge import CvBridge 
from sensor_msgs.msg import Image

rospy.init_node('color_detector')

def callback(msg):
    bridge = CvBridge()
    cv_array = bridge.imgmsg_to_cv2(msg)
    #rospy.loginfo(cv_array)
    resize = cv2.resize(cv_array,dsize=(495,270))
    cv2.imshow("image",resize)
    cv2.waitKey(1)
    msg2 = bridge.cv2_to_imgmsg(resize)
    #rospy.loginfo(msg2)

sub = rospy.Subscriber('/cv_camera/image_raw', Image, callback)
pub = rospy.Publisher('msg2', Image)

rospy.spin()
