from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from mainwindow import Ui_MainWindow
import sys
import zmq
import time
import numpy as np
import base64
import cv2
import io
from PIL import Image


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

            # Timer init  
            # calling ( readData ) every 1000 milliseconds
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.readData)

            # Socket connection ( client )
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://127.0.0.1:5000")  # local host
        # self.socket.connect("tcp://192.168.214.246:8888")  # mobile hotspot
        self.pixmap = QPixmap("testtt.jpg")




            # Push buttons commands
        self.ui.arrow_up.clicked.connect(lambda: self.sendData("forward"))
        self.ui.arrow_down.clicked.connect(lambda: self.sendData("backward"))
        self.ui.arrow_left.clicked.connect(lambda: self.sendData("left"))
        self.ui.arrow_right.clicked.connect(lambda: self.sendData("right"))



    def sendData(self, data):
        self.socket.send_string(data)
      

    def readData(self):
   
        msg = self.socket.recv(flags= zmq.NOBLOCK)

        # decoding the string into a jpg image and saving it
        decoded = base64.b64decode(msg)
        data = io.BytesIO(decoded)
        converted = Image.open(data)
        converted.save("testtt.jpg")

        # this delay is just for testing
        time.sleep(1)

        # putting the image into the GUI
        self.ui.label.setPixmap(self.pixmap)



        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()