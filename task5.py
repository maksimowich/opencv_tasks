import cv2


img = cv2.imread('fixtures/task5/img5.jpg')
contur1 = cv2.Sobel(img, -1, 1, 1)
while True:
    cv2.imshow('contur1', contur1)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

contur2 = cv2.Canny(img, 10, 250)
while True:
    cv2.imshow('contur1', contur2)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
