#code to detect edge in image 
#Image_processing using python in Google colab
 

import numpy as np
from skimage.io import imread, imshow
from skimage.filters import prewitt_h,prewitt_v
import matplotlib.pyplot as plt
%matplotlib inline

#reading the image 
image = imread('/Day1c3.jpg',as_gray=True)

#calculating horizontal edges using prewitt kernel
edges_prewitt_horizontal = prewitt_h(image)
#calculating vertical edges using prewitt kernel
edges_prewitt_vertical = prewitt_v(image)

#imshow(edges_prewitt_vertical, cmap='gray')
imshow(edges_prewitt_horizontal,cmap='gray')
