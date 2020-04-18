import cv2
import numpy as np
class tracker(object):
    val,drawboard = [None]*2,[]
    def __init__(self,bgimage):
        tracker.drawboard = np.zeros_like(bgimage).astype(np.uint8)
        self.erase()
        self.background = cv2.GaussianBlur(bgimage, (5, 5), 0)
        self.background = (self.background//128) * 255
        self.cont = True
        
    def preprocess(self,img):
        self.img = img.copy()
        self.img = cv2.GaussianBlur(self.img,(5,5),0)
        obj = self.obj_filter()
        matrix = np.transpose(np.nonzero(obj))
        if len(matrix) > 0:
            tracker.val[0] = matrix[0]
        else:
            tracker.val=[None]*2
        
        return obj
        
    def obj_filter(self):
           
        #Method-1(50%  success)        
        #Sobel Filtration

        #Method-2
        obj = (self.img//128)*255
        obj[obj == self.background] == [0,0,0]
        obj = cv2.bitwise_not(cv2.cvtColor(obj,cv2.COLOR_BGR2GRAY))
        return obj
    
    def draw(self):
        #Tracker.val contains all the points

        if tracker.val[0] is not None and self.cont:
        
            if tracker.val[1] is not None:
                cv2.line(tracker.drawboard,(tracker.val[1][1],tracker.val[1][0]), (tracker.val[0][1],tracker.val[0][0]) , self.color,thickness=6)
            else:
                self.color = self.img[tracker.val[0][0]][tracker.val[0][1]]
                self.color = tuple([int(x) for x in self.color])
                cv2.circle(tracker.drawboard,(tracker.val[0][1],tracker.val[0][0]),3,self.color,thickness=-1)
            tracker.val[1] = tracker.val[0]

        return tracker.drawboard

    def erase(self):
        #Erasing stuff
        tracker.drawboard.fill(255)
        tracker.val=[None]*2
        self.color = []
        
    def pause(self):
        self.cont = False if self.cont else True
        tracker.val=[None]*2
