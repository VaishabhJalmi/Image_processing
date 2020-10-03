# Extracting RGB values.  
# Here we have randomly chosen a pixel 
image = cv2.imread('photo.jpg') 
# by passing in 100, 100 for height and width. 
(B, G, R) = image[100, 100] 
  
# Displaying the pixel values 
print("R = {}, G = {}, B = {}".format(R, G, B)) 
  
# the value for a specific channel 
B = image[100, 100, 0] 
print("B = {}".format(B)) 
