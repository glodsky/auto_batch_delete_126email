import pyautogui
import cv2
import aircv as av
from PIL import ImageGrab
import numpy as np
import time
import datetime

source = ImageGrab.grab()
p1 = cv2.cvtColor(np.array(source),cv2.COLOR_RGB2BGR)
p2 = av.imread("./choose.png")
pos = av.find_template(p1,p2)
a1,a2 = pos['result']
def do(a1,a2):
    pyautogui.moveTo(a1,a2,duration=0.5)
    #pyautogui.moveRel(10,20)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveRel(50,0)
    pyautogui.click()
    time.sleep(3)
 
    
for i in range(1,135): # 135 is my total pages number of emails , one page includes 100 emails
    do(a1,a2)
    print("[%s] Deleted %d/134\n"%(datetime.datetime.now().strftime('%H:%M:%S'),i))
    
