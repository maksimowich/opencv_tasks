import cv2


img = cv2.imread('fixtures/task5/img5.jpg')
contur1 = cv2.Sobel(img, -1, 1, 1)
cv2.imshow('contur1', contur1)
cv2.waitKey(0)

contur2 = cv2.Canny(img, 10, 250)
cv2.imshow('contur1', contur2)
cv2.waitKey(0)
