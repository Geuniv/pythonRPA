import cv2
import numpy as np

# --① 그레이 스케일로 영상 읽기
img = cv2.imread('../img/abnormal.jpg', cv2.IMREAD_GRAYSCALE)

# --② OpenCV API를 이용한 정규화
img_norm2 = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)


cv2.imshow('Before', img)
cv2.imshow('cv2.normalize', img_norm2)
cv2.waitKey()
cv2.destroyAllWindows()