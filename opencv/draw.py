import cv2
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')

#colouring
blank[:] = 255,0,0
cv2.imshow('blue',blank)

blank[:] = 0,255,0
cv2.imshow('green',blank)

blank[:] = 0,0,255
cv2.imshow('red',blank)
rectangle

blank[:] = 0,0,0

cv2.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) #thickness = -1 for filling
cv2.imshow('rectangle',blank)

#circle

cv2.circle(blank, (250,250),60,(255,0,0),thickness=-1)
cv2.imshow('circle',blank)

#line

cv2.line(blank,(0,0),(250,250),(0,0,255),thickness=4)
cv2.imshow('line',blank)

#text

cv2.putText(blank,'Welcome',(250,250),cv2.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv2.imshow('text',blank)

cv2.waitKey(0)
