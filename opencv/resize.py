import cv2

def rescale(frame,scale = 0.75):
    #for everything
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
#
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
#

def changeRes(width,height):
    #only for live video
    capture.set(3,width)
    capture.set(4,height)

img = cv2.imread('pics/pen.jpg')
img = rescale(img,0.1)
cv2.imshow('Bird',img)
cv2.waitKey(0)
capture = cv2.VideoCapture('vids/car.mp4')
while True:
    isTrue, frame = capture.read()
#
    frame_rescale = rescale(frame,0.5)
    cv2.imshow("Vid", frame_rescale)
#
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
#
capture.release()
cv2.deleteAllWindows()