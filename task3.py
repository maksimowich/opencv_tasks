import cv2


img = cv2.imread('fixtures/task3/img1.jpg')

def rotate_img(img, angle):
    (h, w) = img.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_img = cv2.warpAffine(img, M, (w, h))
    return rotated_img


img_rotated_cw = rotate_img(img, 58)
cv2.imshow('TITEL', img_rotated_cw)
cv2.waitKey(0)

img_rotated_ccw = rotate_img(img_rotated_cw, -10)
cv2.imshow('TITEL', img_rotated_ccw)
cv2.waitKey(0)

img2 = abs(img - img_rotated_ccw) * 10
cv2.imshow('TITEL', img2)
cv2.waitKey(0)
