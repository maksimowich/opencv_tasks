import cv2


cap = cv2.VideoCapture(0)

success, img = cap.read()
cv2.imshow('TITLE', img)
cv2.waitKey(0)

