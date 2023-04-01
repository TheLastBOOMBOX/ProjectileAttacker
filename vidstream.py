
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
# xbox kinect?
webcam = cv.VideoCapture(0) #webcam is the video CVideoCapture, the value 0 indicates the camera
if not webcam.isOpened():
    print("Camera not opened")
    exit()
while True:
    webcamOn, frame = webcam.read() # .read() returns a tuple, containing a bool for if the webcam is on, and the frame captured
    if not webcamOn: # if webcam is not on (for whatever reason)
        print("Error, Frame not captured")
        break
    
    b = frame[:,:,0]
    g = frame[:,:,1]
    r = frame[:,:,2]
    cv.imshow("frame", b) # create window with the title frame, that shows the webcam capture immediatle
    next = cv.waitKey(0)


    rows, columns, channels = frame.shape
    if next == ord("q"):
        print(rows,columns,channels)
        break
    previousFrame = frame
    if next == ord("y"):
        cv.imshow("frame", b)
        cv.imshow("frame", g)
        cv.imshow("frame", r)
        print(rows,columns,channels)
        cv.waitKey(0)


webcam.release() #Release the VideoCapture 
cv.destroyAllWindows()
