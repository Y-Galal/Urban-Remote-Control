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
        # Camera Streaming with 30 FPS (ceil(1000/30))
        self.timer.setInterval(16)
        self.timer.start()
        self.timer.timeout.connect(self.readData)

        # Socket connection ( client )
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://127.0.0.1:5000")  # local host
        # self.socket.connect("tcp://192.168.214.246:8888")  # mobile hotspot
        self.pixmap = QPixmap("camera_image.jpg")




        # Push buttons commands
        self.ui.arrow_up.clicked.connect(lambda: self.sendData("forward"))
        self.ui.arrow_down.clicked.connect(lambda: self.sendData("backward"))
        self.ui.arrow_left.clicked.connect(lambda: self.sendData("left"))
        self.ui.arrow_right.clicked.connect(lambda: self.sendData("right"))

    def showImage(self):
        # Putting the image into the GUI
        self.ui.label.setPixmap(self.pixmap)

    def Decode(self, testmsg):
        # Decoding the string from Base64 into a jpg format again
        decoded = base64.b64decode(testmsg)

        # Decode the string into np.uint8 data stream
        decoded = np.fromstring(decoded,dtype=np.uint8)

        # Decode OpenCV with parameter '1' to make it RGB
        # To make it BW, use '0'
        data = cv2.imdecode(decoded,1)

        # Show the Video stream in a window
        cv2.imshow("Vehicle Stream",data)

        # In order to be able to close the window
        cv2.waitKey(1)

    def sendData(self, data):
        self.socket.send_string(data)

    def readData(self):
        msg = self.socket.recv(flags= zmq.NOBLOCK)
        self.Decode(msg)
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()