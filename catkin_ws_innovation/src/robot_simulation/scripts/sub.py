#!/usr/bin/env python3
# Copyright (c) 2015, Rethink Robotics, Inc.

# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

# Using this OpenCV2 tutorial for saving Images:
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
# from sip import Buffer

import zmq
import time
from zmq import Poller
from base64 import b64encode

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.1:5000")
poller = zmq.Poller()
poller.register(socket, flags=zmq.POLLIN)



# Instantiate CvBridge
bridge = CvBridge()

def image_callback(msg):
    print("Received an image!")

    # Convert your ROS Image message to OpenCV2
    cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")

    # Compress the Image to .jpg format
    encoded,mesg = cv2.imencode(".jpg",cv2_img)
    
    # Encode the Message as Base64 and send it over the ZMQ network
    strng = b64encode(mesg)
    socket.send(strng)





#    print(cv2_img.reshape(-1))
#    data= cv2_img.reshape(-1)
#    encoded_string = b64encode(cv2_img)
#    print(encoded_string)
#    socket.send(encoded_string)
#    socket.send_string(encoded_string.decode('utf-8'))




    socks = dict(poller.poll(150))
    if socks.get(socket) == zmq.POLLIN:
        msg= socket.recv_string(flags=zmq.NOBLOCK)
        print(msg)


def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/robot/camera1/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()
