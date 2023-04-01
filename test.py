import cv2 as cv
import numpy as np
img = cv.imread(".\Pictures\\testcard.png")
assert img is not None, "file could not be read, check with os.path.exists()"
cv.imshow("image",img)
cv.waitKey(0) 
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
rows, columns, channels = img.shape 
print(rows,columns,channels)
cv.rectangle(img,(0,0),(columns-1,rows-1),(0,0,255),2)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows