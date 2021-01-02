import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread('/content/drive/MyDrive/Colab Notebooks/Tiger.jpg',0)
print("\n Orignal Image                                      GaussianBlur")
blur = cv2.GaussianBlur(img,(5,5),0)
output=cv2.hconcat([img,blur])
cv2_imshow(output)
