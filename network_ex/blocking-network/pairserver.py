import zmq
import random
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.1:8888")

while True:
	smsg = input('Enter your message: ')
	socket.send_string(smsg)
	msg = socket.recv_string()
	print ('From client:',msg)