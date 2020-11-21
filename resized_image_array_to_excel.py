import cv2
from google.colab.patches import cv2_imshow  #only for google colab users

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


#Code to convert image to 3d array format matrix and store arrays 

# Import the necessary libraries
import cv2
from PIL import Image 
from numpy import asarray 

# import numpy library 
import numpy 

img =  resized

# Converting color image to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# load the image and convert into  
# numpy array 
numpydata = asarray(gray)

#dimensions = img.shape
#print(img.shape) 
#print(gray.shape) 

# data 
print(numpydata)
print(gray.size)

# import pandas as pd 
import pandas as pd 
  
# list of strings 
lst = numpydata
  
# Calling DataFrame constructor on list 
df = pd.DataFrame(lst) 
print(df) 

#TO save data in excel
df.to_excel('your path file here.xlsx', sheet_name='your_file_name')
