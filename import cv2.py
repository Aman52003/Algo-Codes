import cv2 as a 
import numpy as np
from matplotlib import pyplot as plt

img = a.imread('watch.jpg',a.IMREAD_GRAYSCALE)
a.imshow('image',img)
a.waitKey(0)
a.destroyAllWindows()