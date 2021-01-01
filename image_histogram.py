import cv2
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt

gray_image = cv2.imread("/content/drive/MyDrive/lmages for lp/Animal_Tiger.jpg", cv2.IMREAD_GRAYSCALE)
print("lmage shape ",gray_image.shape) 
cv2_imshow(gray_image)
print("\n\nTo plot histogram of a given gray level image")
plt.hist(gray_image .ravel(), bins=255)
plt.show()
