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
import serial


# --- Network Init ---

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.1:5000")
poller = zmq.Poller()
poller.register(socket, flags=zmq.POLLIN)


# --- Decoding Init ---

Throttle=0
Steering=0

serialPort=0
maxThrottle = 15
minThrottle = -5

maxSteering =  26
minSteering = -24



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


    #Non-Blocking receiving commands from GUI
    try:       
        msg= socket.recv_string(flags=zmq.NOBLOCK) #Trying to receive from GUI
        print(msg)                                 #If the data was there and received, print it
    except zmq.Again as e:                 #zmq.Again is the exception fired if there wasn't data received from the GUI
    #Nothing is processed here but we should handle the exception.
        pass
    
    ################ Receiving with 150ms polling (causes fps lag) ################
    #socks = dict(poller.poll(150))
    #if socks.get(socket) == zmq.POLLIN:
    #   msg= socket.recv_string(flags=zmq.NOBLOCK)
    #  print(msg)
    ###############################################################################


# --- Decoding Layer Functions ---

def serialCommunication():
    global serialPort
    serialPort= serial.Serial(port = "/dev/ttyACM0", baudrate=115200)
    #serialPort.open()


def decoding(decision):
    message=''
    global Throttle
    global Steering
    if decision == 'w':
        if Throttle < maxThrottle:
            Throttle = Throttle+1
        message = str(Throttle) + 't'
    elif decision == 'a':
        if Steering > minSteering:
            Steering = Steering-1
        message = str(Steering) + 'o'
    elif decision == 's':
        if Throttle > minThrottle:
            Throttle = Throttle-1
        message = str(Throttle) + 't'
    elif decision == 'd':
        if Steering < maxSteering:
            Steering = Steering+1
        message = str(Steering) + 'o'

    #Sizing the packet before sending it (4 bytes/packet)
    if message[0] == '-' and len(message) == 3:
        message = message[0] + '0' + message[1:]
    elif len(message) == 3:
        message = '0' + message
    elif len(message) == 2:
        message = '00'+ message      #004o can be executed correctly in state decode????
   
        
        
    #    print(message)
    #    message = message.encode('ascii', 'ignore')
    #    serialPort.write(message)





def main():
    # --- Serial Communication Init ---
    #    serialCommunication()

    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/robot/camera1/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()
