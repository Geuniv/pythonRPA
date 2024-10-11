import cv2
import numpy as np

# --① 대상 영상으로 그레이 스케일로 읽기
img = cv2.imread('../img/yate.jpg', cv2.IMREAD_GRAYSCALE)

# --② OpenCV API로 이퀄라이즈 히스토그램 적용
img3 = cv2.equalizeHist(img)

cv2.imshow('Before', img)
cv2.imshow('cv2.equalizeHist()', img3)
cv2.waitKey()
cv2.destroyAllWindows()