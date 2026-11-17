"""
SBS format Data-Matrix Decoder
"""
import cv2 as cv #image detection
import zxingcpp #decoding
from matplotlib import pyplot as plt #for comparing photos
import numpy as np #math
#Python Packages Installed

img = cv.imread('testphotos/TESTIMAGE.jpg', cv.IMREAD_GRAYSCALE)
#reads the image and applies grayscale

assert img is not None, "file could not be read, check with os.path.exists()"
#message if image isn't found

img = cv.pyrUp(img,5)
#OpenCV upscaling

ret,threshold = cv.threshold(img,130,255,cv.THRESH_BINARY)
#Apply binary threshold to make image either black or white
#num1 is the cut-off, num2 makes the rest black

#========================IGNORE==================================#
#just plots picture for testing, remove once done to improve time

titles = ['Original Image', 'Edited Image']
images = [img, threshold]

for i in range(2):
    plt.subplot(2, 1, i + 1), plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

#===============================================================#

results = (zxingcpp.read_barcodes(
threshold, formats = zxingcpp.BarcodeFormat.DataMatrix))
#zxing decodes the data matrix barcodes in C++ and saves results as an array

color = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
#convert the grayscale image back to color to draw the red boxes

#=============code location, numbering and boxing====================

codes = []
#list to store (x, y, text) for each code

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

GAP = 50
#pixels. Codes within this much of the top code's y are in the same row

ordered = []
#new array for the ordered codes

row_num = 0
#for counting the amount of rows

cols = 0
#for counting number of columns

while codes:
    top = min(c[1] for c in codes)
    #finds the top most y value

    row = [c for c in codes if c[1] - top < GAP]
    #find all the codes in that row

    row.sort(key=lambda c: c[0])
    #sorts list lowest x first

    cols = max(cols, len(row))
    #find the biggest row and count the codes in that row to get columns

    ordered += row
    #save to the new list

    codes = [c for c in codes if c not in row]
    #remove them from the old list
    #so that when it loops the newest top left is on the second row

    row_num = row_num + 1

print("rows:", row_num)
#number of rows

print("cols:", cols)
#number of columns

if max(cols, len(row)) != min(cols, len(row)):
    print("missing code on column:", min(cols, len(row)))
    #detect missing code and state the column

for n, c in enumerate(ordered, 1):
    print(n, c[2])
    #prints the ordered codes
#==============================================================================

cv.imwrite("Found_Codes.png", color)
#makes new file called "Found_Codes"

print("Found:", len(results))
#Counts the items in the list and returns the amount and saves as results

#if __name__ == "__main__":
#anything inside this statement isn't passed through when imported