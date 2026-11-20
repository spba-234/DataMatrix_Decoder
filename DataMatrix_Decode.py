"""
SBS format Data-Matrix Decoder
"""
from math import sqrt

import cv2 as cv #image detection
import zxingcpp #decoding
from matplotlib import pyplot as plt #for comparing photos
import numpy as np #math
#Python Packages Installed

#####################################################################

img = cv.imread('testphotos/TESTIMAGE.jpg', cv.IMREAD_GRAYSCALE)
#reads the image and applies grayscale

assert img is not None, "file could not be read, check with os.path.exists()"
#message if image isn't found

img = cv.pyrUp(img,5)
#OpenCV upscaling

ret,threshold = cv.threshold(img,130,255,cv.THRESH_BINARY)
#Apply binary threshold to make image either black or white
#num1 is the cut-off, num2 makes the rest black

######################################################################
#Below just plots picture for testing
#removable

titles = ['Original Image', 'Edited Image']
images = [img, threshold]

for i in range(2):
    plt.subplot(2, 1, i + 1), plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

########################################################################
#makes the red boxes around the codes

results = (zxingcpp.read_barcodes(
threshold, formats = zxingcpp.BarcodeFormat.DataMatrix))
#zxing decodes the data matrix barcodes in C++ and saves results as an array

color = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
#convert the grayscale image back to color to draw the red boxes

####################################################################################

options = [6, 12, 24, 96, 384, 1536]
ER = len(results)
expected_result = min(options, key=lambda o: abs(o - ER))
print(expected_result)
#out of SBS formatted options round up to nearest

###################################################################################
#find position of each code

codes = []
#list to store (x, y, text) for each code

coordinates = []
#list to store just x and y

for r in results:

    position = r.position
    #updates position in for loop

    pts = np.array([(c.x, c.y) for c in (position.top_left, position.top_right, position.bottom_right, position.bottom_left)], np.int32)
    #gets position of each corner

    cv.polylines(color, [pts], True, (0, 0, 255), 2)
    #connects the points of each corner

    cx = (position.top_left.x + position.bottom_right.x) / 2
    cy = (position.top_left.y + position.bottom_right.y) / 2
    #find the average position of each code using two corners to find center

    codes.append((cx, cy, r.text))
    #saves the position and text together

    #coordinates.append((cx, cy))
    #save just coordinates

cv.imwrite("Found_Codes.png", color)
#makes new file called "Found_Codes"

###############################################################################
#determine columns and rows and where missing values are

#coordinate_list = (sorted(coordinates))
#sorts coordinates array by smallest x first

x = 0
#counting variable for miny[x]

rows = 0
#counting columns

for i in codes:
    rows += 1
    #add one to column count

    miny = sorted(([i[1] for i in codes]))
    #sort miny for smallest y coordinate first

    if x >= len(miny):
        break
        #break if x is greater than miny list

    gap = miny[x] + (len(results) / 2) + 50
    #adjust as needed gap for what is in the same row

    while x < len(miny) and miny[x] <= gap:
        #loop while x is within range of miny

        print("miny:", miny[x], "gap:", gap)
        #print miny and gap

        x+=1
        #increase x

    print("row:", rows)

print("total rows:", rows - 1)
print("total columns:", expected_result / (rows - 1))

########################################################################

print("Found:", len(results))
#Counts the items in the list and returns the amount and saves as results

#if __name__ == "__main__":
#anything inside this statement isn't passed through when imported