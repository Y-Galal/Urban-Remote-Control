# Decoding layer

import serial

Throttle=0
Steering=0

serialPort=0
maxThrottle = 15
minThrottle = -5

maxSteering =  26
minSteering = -24

# --- Decoding Layer Functions ---

# function to initialize the serial port with TivaC
def serialCommunicationInit():
    global serialPort
    serialPort= serial.Serial(port = "/dev/ttyACM0", baudrate=115200)

# Function to decode the decision from (w-a-s-d) and sends it using the serial port
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
     
    #   print(message)
    #    message = message.encode('ascii', 'ignore')
    #    serialPort.write(message)


