import cv2


img = cv2.imread('fixtures/task3/img1.jpg')


img_rotated_cw = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
while True:
    cv2.imshow('TITEL', img_rotated_cw)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


img_rotated_ccw = cv2.rotate(img_rotated_cw, cv2.ROTATE_90_COUNTERCLOCKWISE)
while True:
    cv2.imshow('TITEL', img_rotated_ccw)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


img2 = abs(img - img_rotated_ccw) * 10
while True:
    cv2.imshow('TITEL', img2)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
