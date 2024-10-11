import cv2
import numpy as np

img = cv2.imread('../img/girl.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR을 그레이 스케일로 변경 ---①
cv2.imshow('original', img)
cv2.imshow('gray', gray)

cv2.waitKey(0)
cv2.destroAllWindows()