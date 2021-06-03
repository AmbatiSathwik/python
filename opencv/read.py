import cv2

#reading img
img = cv2.imread('pics/bird.jpg')
cv2.imshow('Bird',img)
#reading vids
capture = cv2.VideoCapture('vids/car.mp4')
while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video', frame)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.deleteAllWindows()
