#import cv2
import pyzed.sl as sl

# Create a ZED camera object
camera = sl.Camera()
 

# Set configuration parameters for the camera
# (Resolution, FPS ,Brightness, contrast, saturation.. etc)
init_params = sl.InitParameters()
# Resoltuion values: HD2K, HD1080,HD720, VGA
init_params.camera_resolution = sl.RESOLUTION.HD720
# FPS values 15, 30, 60, 100
init_params.camera_fps = 60

# Openning the camera in order to take shots
err = zed.open(init_params)
if err != sl.ERROR_CODE.SUCCESS:
    print("Error openning the camera")
    exit()

# Get camera information (serial number)
zed_serial = zed.get_camera_information().serial_number
print("Hello! This is my serial number: {}".format(zed_serial))

# Capture Frames in order to publish them on ros topic
# Grab an image
# Those runtime parameters can be adjusted, for the sake of simplicity 
# we just use default
# A new image is available if grab() returns ERROR_CODE.SUCCESS
image = sl.Mat()
runtime_parameters = sl.RuntimeParameters()
while true:
    # Grab an image, a RuntimeParameters object must be given to grab()
    if camera.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
        # A new image is available if grab() returns ERROR_CODE.SUCCESS
        cam.retrieve_image(mat, sl.VIEW.LEFT)
        timestamp = zed.get_timestamp(sl.TIME_REFERENCE.IMAGE)  # Get the image timestamp
        #printing image data
        print("Image resolution: {0} x {1} || Image timestamp: {2}\n".format(image.get_width(), image.get_height(), timestamp.get_milliseconds()))

        #we can use opencv to make a window and view out image
        #cv2.imshow("ZED", mat.get_data())

        
#After grabbing an image, we can process and then publish it in a ros topic.

#Close the camera
camera.close()