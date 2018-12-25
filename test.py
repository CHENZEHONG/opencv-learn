import cv2 as cv
import numpy as np 


def video_demo():
    # 摄像头
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        # 摄像头反转    1/-1 为上下反转
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    # np.array 
    print(np.array(image))


# 读取图片
src = cv.imread('/Users/gzend/Desktop/vuex.png')
# 窗口
cv.imshow("input image", src)
# video_demo()
get_image_info(src)

# 灰度图
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
# 写入result.png文件
cv.imwrite('/Users/gzend/Desktop/result.png',gray)

cv.waitKey(0)


cv.destroyAllWindows()
