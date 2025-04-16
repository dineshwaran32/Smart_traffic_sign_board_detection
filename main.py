import #Import only if not previously imported
import cv2
import numpy as np
rows,cols,ch = image.shape
pts1 = np.float32([[,],[,],[,]])
pts2 = np.float32([[,],[,],[,]])
M = cv2.getAffineTransform(pts1,pts2)
resultimg = cv2.warpAffine(image,M,(cols,rows))