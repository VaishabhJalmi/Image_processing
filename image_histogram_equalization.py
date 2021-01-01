import cv2 
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

img = cv2.imread("/content/drive/MyDrive/lmages for lp/Animal_Tiger.jpg",0)
print("orignal input image"  )
cv2_imshow(img)

equ = cv2.equalizeHist(img)

cv2_imshow(equ)
plt.hist(equ.ravel(), bins=255)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
