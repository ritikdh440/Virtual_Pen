import cv2
import numpy as np
class tracker(object):
    pimg = []
    def __init__(self,img):
        self.img = img

    def preprocess(self):
        tracker.pimg = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        #tracker.pimg = cv2.GaussianBlur(tracker.pimg, (5, 5), 0)
        ref = np.min(tracker.pimg)
        min = ref+10 if ref < 50 else 0
        #ret,tracker.pimg = cv2.threshold(tracker.pimg,min,255,cv2.THRESH_BINARY)
        #return tracker.pimg

        return self.img