import cv2
import numpy as np
class tracker(object):
    pimg = []
    val = []
    fimg = []
    def __init__(self,bgimage):
        self.erase()
        self.background = bgimage

    def preprocess(self,img):
        tracker.pimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        tracker.pimg = cv2.GaussianBlur(tracker.pimg, (5, 5), 0)
        sobel = self.sobel()
        matrix = np.transpose(np.nonzero(sobel))
        if len(matrix) > 0:
            tracker.val.append(matrix[0])
        return tracker.pimg,sobel
        
    def sobel(self):
        sobelx = cv2.Sobel(tracker.pimg,cv2.CV_16S,1,0)
        sobely = cv2.Sobel(tracker.pimg,cv2.CV_16S,0,1)
        sobel = np.uint8(np.hypot(sobelx,sobely))
        sobel[sobel <= 150] = 0
        return sobel
    
    def draw(self):
        i = len(tracker.val)
        if i:
            i -= 1
            if i != 0:
                cv2.line(tracker.fimg,(tracker.val[i-1][1],tracker.val[i-1][0]), (tracker.val[i][1],tracker.val[i][0]) , [70,70,200],thickness=10)
            else:
                cv2.circle(tracker.fimg,(tracker.val[i][1],tracker.val[i][0]),10,[100,100,200],thickness=-1)

        return tracker.fimg

    def erase(self):
        tracker.fimg = np.zeros((480,720,3),dtype=np.uint8)
        tracker.fimg.fill(255)
        tracker.val = []