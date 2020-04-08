import cv2
import lib_track as tracker
from lib_edge import edge
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
    sample = getframe()
    edge = edge(sample)
    edge.getVertex()

    while True:
        ret,frame = cam.read()
        frame = edge.change_perspect(frame)
        cv2.imshow('preview',frame)
        if cv2.waitKey(1) != -1:
            break
    
    cam.release()
    cv2.destroyAllWindows()



