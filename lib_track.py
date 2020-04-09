import cv2
import numpy as np
class tracker(object):
    pimg = []
    def __init__(self,img):
        self.img = img

    def preprocess(self):
        tracker.pimg = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        tracker.pimg = cv2.GaussianBlur(tracker.pimg, (5, 5), 0)
        sobel = self.sobel()
        return self.img

     def sobel(self):
        sobelx = cv2.Sobel(tracker.pimg,cv2.CV_16S,1,0)
        sobely = cv2.Sobel(tracker.pimg,cv2.CV_16S,0,1)
        sobel = np.uint8(np.hypot(sobelx,sobely))
        mean = np.mean(sobel)
        sobel[sobel <= mean] = 0
        return sobel