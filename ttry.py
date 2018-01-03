
import numpy as np
from PIL import ImageGrab
from pyautogui import press
import cv2
import time

while(True):
    printscreen_pil =  ImageGrab.grab(bbox=(700,180,1000,326))
    printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
    .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
    printscreen_numpy =255-printscreen_numpy
    i = np.array(printscreen_numpy)
##    cv2.imshow('window',printscreen_numpy )
##    print(i[105 , 269])
##    print(i[115 , 269])
##    print(i[117 , 275])
    if i[105 , 269][0] >= 80 or i[135 , 269][0] >= 80 or i[125 , 269][0] >= 80 or i[145 , 269][0] >= 80 or i[105 , 209][0] >= 80 or i[139 , 209][0] >= 80:
        time.sleep(0.2)
        press('space')
        
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

