import cv2
import numpy as np
class tracker(object):
    pimg = []
    def __init__(self):
        pass

    def preprocess(self,img):
        tracker.pimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        tracker.pimg = cv2.GaussianBlur(tracker.pimg, (5, 5), 0)
        sobel = self.sobel()
        matrix = np.transpose(np.nonzero(sobel))
        if len(matrix) > 0:
            return matrix[0],tracker.pimg,sobel
        else:
            return None,tracker.pimg,sobel

    def sobel(self):
        sobelx = cv2.Sobel(tracker.pimg,cv2.CV_16S,1,0)
        sobely = cv2.Sobel(tracker.pimg,cv2.CV_16S,0,1)
        sobel = np.uint8(np.hypot(sobelx,sobely))
        sobel[sobel <= 150] = 0
        return sobel
    
    def draw(self,matrix,frame):
        if matrix is not None:
            ln = len(matrix)
            for x in range(0,ln-1):
                frame = cv2.line(frame,(matrix[x][1],matrix[x][0]), (matrix[x+1][1],matrix[x+1][0]) , [70,70,200],thickness=10)
                #cv2.circle(self.img,(matrix[x][1],matrix[x][0]),10,[100,100,200],thickness=-1)
            return frame