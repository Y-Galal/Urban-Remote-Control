import zmq
import time


context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:5000")

while True:
    socket.send_string('Client Sending')
    msg = socket.recv_string()
    print(msg)
