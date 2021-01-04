import serial

Throttle=0
Steering=0

serialPort=0
maxThrottle = 15
minThrottle = -5

maxSteering =  26
minSteering = -24
def serialCommunication():
    global serialPort 
    serialPort= serial.Serial(port = "/dev/ttyACM2", baudrate=115200)
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
        message = '00'+ message         #004o can be executed correctly in state decode????

    
    print(message)
    message = message.encode('ascii', 'ignore')
    serialPort.write(message)

serialCommunication()
while True:
    decision = input('Enter Your Decision: ')   #getting the input from keyboard only for testing purposes
    if decision.lower() == 'w' or decision.lower() == 'a' or decision.lower() == 's'or decision.lower() == 'd':
        decoding(decision.lower())
    else:
        print('W A S D or w a s d only..\n')
    
