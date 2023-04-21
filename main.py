import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import Glare
class ProjectileAttacker(): # co-ordinates the other functions.
    def __init__(self, vidStream, mask) -> None:
        #self.
        pass
        
class Vidstream(): # class that controls how the video capture is utilised by everything else
    def __init__(self) -> None:
        self.vidStream = cv.VideoCapture(0) #vidStream is the video CVideoCapture, the value 1 indicates the external camera
        if not self.vidStream.isOpened():
            print("Camera not opened, check if turret is attached")
            exit()

    def stream(self):
        while True:
            self.webcamOn, self.capture = self.vidStream.read()   
            if not self.webcamOn: # if webcam is not on (for whatever reason)
                print("Error, Frame not captured")
                break
            self.frame()
            feed = self.displayStream() # What the user sees
            if feed == False:
                self.endStream()
                break
            
    def displayStream(self): #displays camera feed to user so they understand what the computer sees
        cv.imshow("frame", self.capture) # create window with the title frame, that shows the webcam capture immediatle
        command = cv.waitKey(1) # waits 1 milisecond for user input, else moves on
        if command == ord("q"): # checks if user wants to end 
            return False
        cv.imshow("guassian", self.guassianFrame) # create window with the title frame, that shows the webcam capture immediatle
        command = cv.waitKey(1) # waits 1 milisecond for user input, else moves on
        if command == ord("q"): # checks if user wants to end 
            return False
        
    def frame(self):
        self.medianFrame = cv.medianBlur(self.capture, 3)
        self.guassianFrame = cv.GaussianBlur(self.medianFrame, (5,5),0,0) 
        self.finalBlur = cv.medianBlur(self.guassianFrame, 5)
        return self.finalBlur

        

    def endStream(self):
        self.vidStream.release() #Release the VideoCapture 
        cv.destroyAllWindows()

        
    def speed(self,target): # Defines capture rate of the program. difers between resting, prediction and movement and 
        pass
class TargetID(): # class that identifies targets in video capture, draws a box around them and finds centre
                  # uses machine learning to identify targets
    def __init__(self,vidstream) -> None:
        pass
class Target(): # class that catorgorises target speed, depth, colour, motion tracking and stages way for path prediction
    def __init__(self,position) -> None:
        pass
    pass
class Prediction(): # class that uses the motion tracking data collected by class 'Target' to predict where target will be
                    # taking into account turret rotation and aiming speed.
    pass
class Turret(): # controls robotics of the turret and shooting
    pass
class HitDetection(): # uses other functions and user nput to determine if and how the target was shot.
                      # will then post results to database, which the program can then use to improve itself 
    pass
class UserInput(): # allows user to manually control and override turret actions
    pass
Test = Vidstream()
Test.stream()