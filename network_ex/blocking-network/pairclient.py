import zmq
import random
import sys
import time

context = zmq.Context()
socket  = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:8888")

while True:
	print ('From Server: ',socket.recv_string())
	msg = input('Enter your message: ')
	socket.send_string(msg)