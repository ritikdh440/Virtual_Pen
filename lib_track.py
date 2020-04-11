import cv2
import numpy as np
class tracker(object):
    pimg = []
    val = []
    fimg = []
    def __init__(self,bgimage):
        self.erase()
        self.background = bgimage
        self.background = cv2.cvtColor(self.background,cv2.COLOR_BGR2GRAY)
        self.background = cv2.GaussianBlur(self.background, (5, 5), 0)
        self.backobj = np.uint8(np.hypot(cv2.Sobel(self.background,cv2.CV_16S,1,0),cv2.Sobel(self.background,cv2.CV_16S,0,1)))
        self.bgmean = np.mean(self.backobj)
        self.bgmax = np.max(self.backobj)
        
    def preprocess(self,img):
        self.img = img.copy()
        tracker.pimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        tracker.pimg = cv2.GaussianBlur(tracker.pimg, (5, 5), 0)
        obj = self.obj_filter()
        matrix = np.transpose(np.nonzero(obj))
        if len(matrix) > 0:
            tracker.val.append(matrix[0])
        else:
            tracker.val=[]
        return tracker.pimg,obj
        
    def obj_filter(self):
        #Method-1(20%  success)        
        sobelx = cv2.Sobel(tracker.pimg,cv2.CV_16S,1,0)
        sobely = cv2.Sobel(tracker.pimg,cv2.CV_16S,0,1)
        obj = np.uint8(np.hypot(sobelx,sobely))

        #Filteration
        obj = cv2.subtract(obj,self.backobj)
        obj[obj < np.mean(obj)] = 0
        # obj[obj < np.max(obj)/2] = 0
        
        return obj
    
    def draw(self):
        i = len(tracker.val)
        if i:
            i -= 1
            if i != 0:
                cv2.line(tracker.fimg,(tracker.val[i-1][1],tracker.val[i-1][0]), (tracker.val[i][1],tracker.val[i][0]) , [70,70,200],thickness=10)
            else:
                cv2.circle(tracker.fimg,(tracker.val[i][1],tracker.val[i][0]),5,[100,100,200],thickness=-1)

        return tracker.fimg

    def erase(self):
        tracker.fimg = np.zeros((480,720,3)).astype(np.uint8)
        tracker.fimg.fill(255)
        tracker.val = []