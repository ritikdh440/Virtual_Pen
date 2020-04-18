import cv2
import numpy as np
class tracker(object):
    pimg,val,fimg = [],[None]*2,[]
    def __init__(self,bgimage):
        tracker.fimg = np.zeros_like(bgimage).astype(np.uint8)
        self.erase()
        # self.background = cv2.GaussianBlur(cv2.cvtColor(bgimage,cv2.COLOR_BGR2GRAY), (5, 5), 0)
        # self.graybg = np.uint8(np.hypot(cv2.Sobel(self.background,cv2.CV_16S,1,0),cv2.Sobel(self.background,cv2.CV_16S,0,1)))
        self.cont = True
        
    def preprocess(self,img):
        self.img = img.copy()
        self.img = cv2.GaussianBlur(self.img,(5,5),0)
        # tracker.pimg = cv2.GaussianBlur(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY), (5, 5), 0)
        # tracker.pimg = cv2.blur(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) , (5,5))
        obj = self.obj_filter()
        matrix = np.transpose(np.nonzero(obj))
        if len(matrix) > 0:
            tracker.val[0] = matrix[0]
        else:
            tracker.val=[None]*2
        
        return obj
        
    def obj_filter(self):
        #Adjust according to noise
        thresh = 20
    
        #Method-1(50%  success)        
        #Sobel Filtration

        #Method-2
        obj = (self.img//128)*255
        obj = cv2.bitwise_not(cv2.cvtColor(obj,cv2.COLOR_BGR2GRAY))
        return obj
    
    def draw(self):
        #Tracker.val contains all the points

        if tracker.val[0] is not None and self.cont:
        
            if tracker.val[1] is not None:
                cv2.line(tracker.fimg,(tracker.val[1][1],tracker.val[1][0]), (tracker.val[0][1],tracker.val[0][0]) , self.color,thickness=6)
            else:
                self.color = self.img[tracker.val[0][0]][tracker.val[0][1]]
                self.color = tuple([int(x) for x in self.color])
                cv2.circle(tracker.fimg,(tracker.val[0][1],tracker.val[0][0]),3,self.color,thickness=-1)
            tracker.val[1] = tracker.val[0]

        return tracker.fimg

    def erase(self):
        #Erasing stuff
        tracker.fimg.fill(255)
        tracker.val=[None]*2
        self.color = []
    
    
    def pause(self):
        self.cont = False if self.cont else True

        tracker.val=[None]*2
