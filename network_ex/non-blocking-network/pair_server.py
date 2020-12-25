import zmq
import time
from zmq import Poller


context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.1:5000")
poller = zmq.Poller()
poller.register(socket, flags=zmq.POLLIN)


while True:
    socket.send_string('Server sending')
    socks = dict(poller.poll(150))
    if socks.get(socket) == zmq.POLLIN:
        msg= socket.recv_string(flags=zmq.NOBLOCK)
        print(msg)
