import cv2
import numpy as np

alpha = 0.5 # 합성에 사용할 알파 값

# ---① 합성에 사용할 영상 읽기
img1 = cv2.imread('../img/wing_wall.jpg')
img2 = cv2.imread('../img/yate.jpg')

# ---② addWeighted() 함수로 알파 블렌딩 적용
dst = cv2.addWeighted(img1, alpha, img2, (1 - alpha), 0)
cv2.imshow('cv2 addWeighted', dst)

cv2.waitKey(0)
cv2.destroAllWindows()