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
        sobelx = cv2.Sobel(self.background,cv2.CV_16S,1,0)
        sobely = cv2.Sobel(self.background,cv2.CV_16S,0,1)
        obj = np.uint8(np.hypot(sobelx,sobely))
        self.bgmean = np.mean(obj)
        self.bgmax = np.max(obj)
        
    def preprocess(self,img):
        self.img = img.copy()
        tracker.pimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        tracker.pimg = cv2.GaussianBlur(tracker.pimg, (5, 5), 0)
        obj,contour = self.obj_filter()
        matrix = np.transpose(np.nonzero(obj))
        if len(matrix) > 0:
            tracker.val.append(matrix[0])
        return tracker.pimg,obj,contour
        
    def obj_filter(self):
        #Method-1(20%  success)        
        sobelx = cv2.Sobel(tracker.pimg,cv2.CV_16S,1,0)
        sobely = cv2.Sobel(tracker.pimg,cv2.CV_16S,0,1)
        
        # obj = np.uint8(np.hypot(sobelx,sobely))
        # obj[obj <= 150] = 0
        # return obj


        #Method-2(Are negatives allowed?)
        rs = cv2.subtract(self.background,tracker.pimg)
        # sobelx = cv2.Sobel(rs,cv2.CV_16S,1,0)
        # sobely = cv2.Sobel(rs,cv2.CV_16S,0,1)
        obj = np.uint8(np.hypot(sobelx,sobely))
        print(np.mean(obj),np.max(obj))
        obj[np.logical_or(np.mean(obj) < self.bgmean, obj < self.bgmax + 10,obj < np.max(obj)/2)] = 0
        # contour = self.getContour(obj)
        return obj,obj
    
    
    def getContour(self,edgeImg):
       
        contours, heirarchy = cv2.findContours(edgeImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # Find level 1 contours
        level1 = []
        if heirarchy is not None:
            for i, tupl in enumerate(heirarchy[0]):
                # Each array is in format (Next, Prev, First child, Parent)
                # Filter the ones without parent
                if tupl[3] == -1:
                    tupl = np.insert(tupl, 0, [i])
                    level1.append(tupl)
            significant = []
            tooSmall = edgeImg.size * 5 / 100 
            
            for tupl in level1:
                contour = contours[tupl[0]]
                area = cv2.contourArea(contour)
                if area > tooSmall:
                    significant.append([contour, area])
                    # Draw the contour on the original image
                    cv2.drawContours(self.img, [contour], 0, (0,255,0),2, cv2.LINE_AA, maxLevel=1)

            significant.sort(key=lambda x: x[1])
        return self.img
 
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
        tracker.fimg = np.zeros((480,720,3)).astype(np.uint8)
        tracker.fimg.fill(255)
        tracker.val = []