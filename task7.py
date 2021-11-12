import cv2
import random
import numpy
import copy


def get_noised_img(img, delta):
    new_img = copy.deepcopy(img)
    sigma = delta ** 0.5
    row, column, colors = img.shape
    deviation = numpy.random.normal(0, sigma, (row, column, colors))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                new_bit = new_img[i][j][k] + deviation[i][j][k] 
            if 0 <= new_bit <= 255:
                new_img[i][j][k] = new_bit
    return new_img


img = cv2.imread('fixtures/task6/img6.png')
noised_img = get_noised_img(img, 10000)
while True:
    cv2.imshow('noise_img', noised_img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

blur_img = cv2.bilateralFilter(noised_img,9,75,75)
while True:
    cv2.imshow('blur_img', blur_img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
