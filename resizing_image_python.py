import cv2
from google.colab.patches import cv2_imshow   #for google colab users

img = cv2.imread('/content/drive/My Drive/FISH_DATASET /DAY3/WTHOUT_ZOOM/IMG_20200828_211224.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
width = 150
height = 150
dim = (width, height)
 
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2_imshow( resized)
#cv2_waitKey(0)
#cv2_destroyAllWindows()
