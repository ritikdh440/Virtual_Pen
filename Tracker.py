import cv2
import numpy as np
from lib_track import tracker
from lib_edge import edge
fframe= []
def init():
    global fframe
    ret,fframe = cam.read()
    fframe = edge.change_perspect(fframe)
    # fframe = cv2.cvtColor(fframe,cv2.COLOR_BGR2GRAY)

def getframe():
     while True:
        ret,frame = cam.read()
        cv2.imshow('Calibrate',frame)
        if cv2.waitKey(1) != -1:
            cv2.destroyAllWindows()
            return frame

#Main Code Starts Here
cam = cv2.VideoCapture(0)

if not(cam.isOpened()):
    print("Error Accessing Camera Object")
else:
    mat = []
    
    sample = getframe()
    edge = edge(sample)
    edge.getVertex()
    init()
    while True:
        #Initializations
        ret,frame = cam.read()

        frame = edge.change_perspect(frame)
        
        # sub_frame = sub(frame)
        # sub_frame = frame
        #track = tracker(sub_frame)
        track = tracker()
        temp,pimg,sobel = track.preprocess(frame)
        
        #Drawing Board
        if temp is not None:
            mat.append(temp)
        frame = track.draw(mat,frame)

        #Image Showing Stuff 
        cv2.imshow('Filtered',sobel)
        cv2.imshow('Drawing Board' , frame)
        #cv2.imshow('Subtracted',sub_frame)
        #Closing Stuff
        key = cv2.waitKey(1)
        if key == 27:
            break
        elif key != -1:
            mat = []
    
    cam.release()
    cv2.destroyAllWindows()



