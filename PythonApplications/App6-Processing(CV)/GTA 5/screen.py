import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import *

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

print('down')
PressKey(W)
time.sleep(3)
print('up')
ReleaseKey(W)

#while(True):
    #screen =  np.array(ImageGrab.grab(bbox=(0, 40, 375, 375)))


    #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    #cv2.waitKey(10)

cv2.destroyAllWindows()
