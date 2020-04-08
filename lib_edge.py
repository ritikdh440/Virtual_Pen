import cv2
import numpy as np

class edge(object):
    vertex = []
    count = 0
    output = (1280,720)
    def __init__(self,img):
        self.img = img

    def getVertex(self):
        cv2.namedWindow('Select Vertex')
        cv2.setMouseCallback('Select Vertex',self.mouseClick)
        #self.img = cv2.flip(self.img,1)
        cv2.imshow('Select Vertex',self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
    def mouseClick(self,event,x,y,flags,param):
        if edge.count == 4:
            return
        
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(self.img,(x,y),4,[0,0,255],thickness=4)
            cv2.imshow('Select Vertex' , self.img)
            edge.vertex.append([x,y])
            edge.count += 1
        
    def change_perspect(self,frame):
        v = edge.vertex
        pts1 = np.float32([[v[0][0],v[0][1]],[v[1][0],v[1][1]],[v[2][0],v[2][1]],[v[3][0],v[3][1]]])
        pts2 = np.float32([[0,0],[1,0],[1,1],[0,1]])
        pts2 = pts2*np.float32(edge.output)
        mat = cv2.getPerspectiveTransform(pts1,pts2)
        frame = cv2.warpPerspective(frame,mat,edge.output)
        return frame