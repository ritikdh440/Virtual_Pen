import cv2
from lib_track import tracker
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
    mat = []
    while True:
        ret,frame = cam.read()
        frame = edge.change_perspect(frame)
        track = tracker(frame)
        cv2.imshow('Original',frame)
        temp = track.preprocess()
        if temp is not None:
            mat.append(temp)
        track.draw(mat) 
        cv2.imshow('Altered',frame)

        key = cv2.waitKey(1)
        if key == 27:
            break
        elif key != -1:
            mat = []
    
    cam.release()
    cv2.destroyAllWindows()



