import cv2 as cv
import numpy as np


# 反转像素
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255-pv
    cv.imshow("pixels_demo", image)


def create_image():
    img = np.zeros([400, 400, 3], np.uint8)
    cv.imshow("new image", img)


# 反转像素 (opencv原生函数执行速度快)
def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse_demo", dst)


src = cv.imread("/Users/gzend/Desktop/vuex.png")

t1 = cv.getTickCount()
access_pixels(src)
t2 = cv.getTickCount()
print((t2-t1)/cv.getTickFrequency()*1000)

create_image()

cv.waitKey(0)
cv.destroyAllWindows()
