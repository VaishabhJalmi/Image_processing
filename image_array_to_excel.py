#To use excel 
!pip install xlsxwriter

#Code to convert image to 3d array format matrix form
# Import the necessary libraries
import cv2
from PIL import Image 
from numpy import asarray 
  
  
# load the image and convert into  
# numpy array 
#img = Image.open('/content/drive/My Drive/FISH_DATASET /DAY1/IMG_20200826_211309.jpg')

img = cv2.imread("/content/drive/My Drive/FISH_DATASET /DAY3/WTHOUT_ZOOM/IMG_20200828_211224.jpg")

# Converting color image to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

numpydata = asarray(gray)
#dimensions = img.shape
print(img.shape) 
print(gray.shape)
print(gray.size)

# data 
print(numpydata) 

# import pandas as pd 
import pandas as pd 
  
# list of strings 
lst = numpydata
  
# Calling DataFrame constructor on list 
df = pd.DataFrame(lst) 
print(df) 

#save file to location path (ready.xlsx)
df.to_excel('ready.xlsx', sheet_name='your_file_name')
