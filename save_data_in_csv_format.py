##Code to convert image to 3d array format matrix and store arrays in csv format

# Import the necessary libraries
import cv2
from PIL import Image 
from numpy import asarray 

# import numpy library 
import numpy 

  
# load the image and convert into  
# numpy array 
#img = Image.open('/content/drive/My Drive/FISH_DATASET /DAY1/IMG_20200826_211309.jpg')

img = cv2.imread("/content/drive/My Drive/FISH_DATASET /DAY2/WITH_ZOOM/IMG_20200827_210552.jpg")

# Converting color image to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

numpydata = asarray(gray)
#dimensions = img.shape
#print(img.shape) 
#print(gray.shape) 

# data 
print(numpydata)


# save array into csv file 
numpy.savetxt("data.csv", numpydata,  
              delimiter = ",")

              
