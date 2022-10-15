import CSV
import pyautogui
import time
org=[]
with open("attt.CSV")as f1:
    data=list(CSV.reader(f1))
pos=pyautogui.moveTo(460,1058,duration=0)
pyautogui.click()
for d in data:
    print(d[0])
    time.sleep(2)
    pyautogui.typewrite(d[0])
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    im2=pyautogui.screenshot(d[0]+'.png')
"

