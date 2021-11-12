import cv2


img = cv2.imread('fixtures/task1/img1.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('TITLE', img)
cv2.waitKey(0)
cv2.imwrite('result_imgs/task1/img1.jpg', img)
    
