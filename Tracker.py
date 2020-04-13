import cv2
from lib_track import tracker
from lib_edge import edge

def init():
    ret,fframe = cam.read()
    fframe = edge.change_perspect(fframe)
    return fframe

def getframe():
     while True:
        ret,frame = cam.read()
        cv2.imshow('Calibrate',frame)
        if cv2.waitKey(1) != -1:
            cv2.destroyAllWindows()
            return frame

#Main Code Starts Here
cam = cv2.VideoCapture(1)

if not(cam.isOpened()):
    print("Error Accessing Camera Object")
else:
    sample = getframe()
    edge = edge(sample)
    edge.getVertex()
    track = tracker(init())

    while True:
        #Initializations
        ret,frame = cam.read()

        frame = edge.change_perspect(frame)
        obj = track.preprocess(frame)
        dboard = track.draw()

        #Image Display(including process images)
        cv2.imshow('Original',frame)
        cv2.imshow('Object' , obj)
        cv2.imshow('Drawing Board' , dboard)

        #Closing Stuff
        key = cv2.waitKey(1)
        if key == 27:
            break
        elif key == 32:
            track.pause()
        elif key != -1:
            track.erase()
    
    cam.release()
    cv2.destroyAllWindows()

