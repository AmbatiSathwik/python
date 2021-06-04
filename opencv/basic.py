import cv2

img = cv2.imread('pics/bird.jpg')
#cv2.imshow('Bird',img)

#Converting to greyscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Bird',gray)

#Blur
blur = cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow('Blur',blur)

#Edge Cascade
edge = cv2.Canny(blur,125,175)
cv2.imshow('Canny',edge)

#Dialation
dialated = cv2.dilate(edge,(5,5),iterations = 1)
cv2.imshow('Dialated',dialated)

#eroded
eroded = cv2.erode(dialated,(5,5),iterations = 1)
cv2.imshow('Eroded',eroded)

#resize
resized = cv2.resize(img, (500,500))
cv2.imshow('Resize',resized)

#croping
crop = resized[50:200 , 200:400]
cv2.imshow('Crop',crop)


cv2.waitKey(0)
