import cv2


img = cv2.imread('fixtures/task4/img4.png')

b, g, r = cv2.split(img)

cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)
cv2.waitKey(0)

merge_img = cv2.merge([b, g, r])
cv2.imshow('merged_img', merge_img)
cv2.waitKey(0)
