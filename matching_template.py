import cv2 as cv
import numpy as np


img = cv.imread("ronaldo.jpg")




cv.imshow("Image", img)
cv.waitKey()
cv.destroyAllWindows()
