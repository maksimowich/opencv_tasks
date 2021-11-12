import cv2


img = cv2.imread('fixtures/task4/img4.png')

b, g, r = cv2.split(img)

while True:
    cv2.imshow('blue', b)
    cv2.imshow('green', g)
    cv2.imshow('red', r)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

merge_img = cv2.merge([b, g, r])
while True:
    cv2.imshow('merged_img', merge_img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

