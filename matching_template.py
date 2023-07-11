import cv2 as cv
import numpy as np


img = cv.imread("ronaldo.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_temp = cv.imread("ball.jpg", 0)

w, h = img_temp.shape[::-1]

res_match = cv.matchTemplate(gray_img, img_temp, cv.TM_CCORR_NORMED)
print(res_match)



threshold = 0.99
pass_thres = np.where(res_match >= threshold)
print(pass_thres)


for temp_pt in zip(*pass_thres[::-1]):
    cv.rectangle(img, temp_pt, (temp_pt[0] + w, temp_pt[1]+h), (255, 0, 0), 2)

cv.imshow("Image", img)
cv.waitKey()
cv.destroyAllWindows()
