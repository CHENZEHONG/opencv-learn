import cv2 as cv


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    # 取值范围 H 0-180 S 0-255 V 0-255
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb", ycrcb)


def extrace_object_demo(images):
    captrue = cv.VideoCapture(0)


src = cv.imread("/Users/gzend/Desktop/vuex.png")
color_space_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
