import sys
sys.path.append('C:\\Users\\silar\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')

import numpy as np
import cv2

path = input("Path of Images:  ")
endPath = input("Endpath: ")
 
for i in range(36):
    if i == 15:
        i + 1
    src = cv2.imread(path + "\\" + str(i) + ".webp", cv2.IMREAD_UNCHANGED)
    print (src)

    #percent by which the image is resized
    scale_percent = 50

    #calculate the 50 percent of original dimensions
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(src, dsize)

    cv2.imwrite(endPath + "\\" + str(i) + ".webp",output) 