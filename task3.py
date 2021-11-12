import cv2


img = cv2.imread('fixtures/task3/img1.jpg')


img_rotated_cw = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('TITEL', img_rotated_cw)
cv2.waitKey(0)

img_rotated_ccw = cv2.rotate(img_rotated_cw, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('TITEL', img_rotated_ccw)
cv2.waitKey(0)

img2 = abs(img - img_rotated_ccw) * 10
cv2.imshow('TITEL', img2)
cv2.waitKey(0)
