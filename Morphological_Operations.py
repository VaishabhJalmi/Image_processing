
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread('/content/drive/MyDrive/lmages for lp/test.bmp',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
print("Orignal Image\n")
cv2_imshow(img )
print("\nErosion Image\n")
cv2_imshow(erosion )
dilation = cv2.dilate(img,kernel,iterations = 1)
print("\n Dilationn Image\n")
cv2_imshow(dilation)

out=img-erosion 
print("\nimg-erosion Image\n")
cv2_imshow(out)
sub2=img-dilation
print("\nimg-dilation Image\n")
cv2_imshow(sub2)


