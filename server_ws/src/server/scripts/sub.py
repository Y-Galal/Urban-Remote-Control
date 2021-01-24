#*********************************************************
#                                                        *
#      Cairo University Shell Eco-Racing Team            *
#      Shell Eco-Marathon 2021 Autonomous System         *
#      Embedded Autonomous Movement Control Sub-team     *
#                                                        *
#           -> Innovation-Award Project <-               *
#*********************************************************

# OpenCV Library 
import cv2
from base64 import b64encode

# rospy for the Subscriber
import rospy

# ROS Image message
from sensor_msgs.msg import Image

# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError

# ZMQ Networking Library
import zmq
from zmq import Poller
import time

# For Serial Communication and Decoding layer
from decoding import decoding
from decoding import serialCommunicationInit

# --- Network Init ---

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.1:5000")
poller = zmq.Poller()
poller.register(socket, flags=zmq.POLLIN)


# Instantiate CvBridge
bridge = CvBridge()

def image_callback(msg):
    # Convert your ROS Image message to OpenCV2
    cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")

    # Compress the Image to .jpg format
    encoded,mesg = cv2.imencode(".jpg",cv2_img)
    
    # Encode the Message as Base64 and send it over the ZMQ network
    strng = b64encode(mesg)
    socket.send(strng)


    #Non-Blocking receiving commands from GUI
    try:       
        msg= socket.recv_string(flags=zmq.NOBLOCK) #Trying to receive from the client GUI
        print(msg)                                 #If the data was there and received, print it
        decoding(msg)
    except zmq.Again as e:                 #zmq.Again is the exception fired if there wasn't data received from the GUI
    #Nothing is processed here but we should handle the exception.
        pass

def main():
    # --- Serial Communication Init ---
    #    serialCommunicationInit()

    rospy.init_node('image_listener')
    # Define your image topic
    # image_topic = "/zed/zed_node/right/image_rect_color"
    image_topic = "/robot/camera1/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()
