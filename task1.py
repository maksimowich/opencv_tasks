import cv2


img = cv2.imread('fixtures/task1/img1.jpg', cv2.IMREAD_UNCHANGED)

while True:
    cv2.imshow('TITLE', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.imwrite('result_imgs/task1/img1.jpg', img)
    
