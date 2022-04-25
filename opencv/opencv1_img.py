import cv2
import numpy as np

img = cv2.imread("resimler/resim2.jpeg")
img[0:100, 0:100] = [255, 255, 255]
cv2.imshow("Resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
