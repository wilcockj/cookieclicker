import os
import pyautogui
import keyboard
import time
import timeit
import pytesseract
import re
#pyautogui.locateCenterOnScreen('image.png')
pyautogui.PAUSE = 0.01
x = 0
'''
while True:
    pyautogui.click(1651,519)
    if((x % 1000) == 0):
        #upgrade location sorted by least expensive upgrade
        pyautogui.click(3008,346)
       
        #clicks the lowest cookie producing mechanism first as they will
        #be most expensive/produce the most
        pyautogui.click(3112,900)
        pyautogui.click(3112,950)
        pyautogui.click(3112,830)
        pyautogui.click(3112,760)
        #pyautogui.click(3112,680)
        #pyautogui.click(3112,620)
        #pyautogui.click(3112,570)
        #pyautogui.click(3112,500)
        #pyautogui.click(3112,440)
    if(keyboard.is_pressed('q')):
        break
    if x == 1001:
        x = 0
    x+=1
'''
'''
cpmimg = pyautogui.screenshot(region=(201,253,150,13))
startcpm = pytesseract.image_to_string(cpmimg, config='tessedit_char_whitelist=0123456789')
rint(startcpm)
seperatedstartcpm = re.split("\s",startcpm)
print(seperatedstartcpm)
if len(seperatedstartcpm) > 1:
    if seperatedstartcpm[1] == 'thousand':
        startcpmint = str(float(seperatedstartcpm[0])*1000)
    elif seperatedstartcpm[1] == 'billion':
        startcpmint = str(float(seperatedstartcpm[0])*1000000000)
    elif seperatedstartcpm[1] == 'million' or seperatedstartcpm[1] == 'milhion':
        startcpmint = str(float(seperatedstartcpm[0])*1000000)
    elif seperatedstartcpm[1] == 'trillion':
        startcpmint = str(float(seperatedstartcpm[0])*1000000000000)
    print(startcpmint)
'''
#windows ver
start_time = timeit.default_timer()
goldencookies = 0
total_time_searching = 0
while True:
    pyautogui.click(200,370)
    if(x == 1000 or  x == 0 or x == 500 or x == 1500):
        search_time = timeit.default_timer()
        im = pyautogui.locateCenterOnScreen('Images/goldencookie.png',confidence=0.7, region=(0,130,1022,603))
        time_to_search = timeit.default_timer()-search_time
        total_time_searching += time_to_search
        if im != None:
            goldencookies = goldencookies + 1
            pyautogui.moveTo(im[0],im[1],.5)
        print("Golden Cookie Coords = " + str(im) + " Time to search = " + str(time_to_search) + " Total Golden Cookies clicked this session = " + str(goldencookies))
        pyautogui.click(im)        
    if(x == 0):
        '''
        #TODO FIX OCR
        #cpmimg2 = pyautogui.screenshot(region=(201,253,150,13))
        cpmimg2 = pyautogui.screenshot(region=(569,505,75,20))
        thacpm = pytesseract.image_to_string(cpmimg2, config='tessedit_char_whitelist=0123456789')
        seperatedcpm = re.split("\s",thacpm)
        cpmimg2.save('out.png')
        print(seperatedcpm)#[0] has number [1] has thousands millions billions etc.
        
        if len(seperatedcpm) > 1:
            newcpmint = 0
            if seperatedcpm[1] == 'thousand':
                newcpmint = str(float(seperatedpm[0])*1000)
            elif seperatedcpm[1] == 'billion':
                newcpmint = str(float(seperatedcpm[0])*1000000000)
            elif seperatedcpm[1] == 'million' or seperatedcpm[1] == 'milhion':
                newcpmint = str(float(seperatedcpm[0])*1000000)
            elif seperatedcpm[1] == 'trillion':
                newcpmint = str(float(seperatedcpm[0])*1000000000000)
            print(newcpmint)
       ''' 
        
        pyautogui.moveTo(1082,287)
        pyautogui.scroll(300)
        time.sleep(.5)
        #upgrade location sorted by least expensive upgrade
        if pyautogui.pixelMatchesColor(1204,190,(8,24,32)):
            print("scroll worked")
            pyautogui.click(1082,287)
            pyautogui.click(1082,287)
            pyautogui.click(1082,287)
            pyautogui.click(1082,287)
        pyautogui.scroll(-200)
        time.sleep(.5)
        #clicks the lowest cookie producing mechanism first as they will
        #be most expensive/produce the most
        pyautogui.click(1082,700)
        time.sleep(.05)
        pyautogui.click(1082,640)
        time.sleep(.05)
        pyautogui.click(1082,580)
        time.sleep(.05)
        pyautogui.click(1082,510)
        time.sleep(.05)
        pyautogui.click(1082,450)
        time.sleep(.05)
        pyautogui.click(1082,390)
        time.sleep(.05)
        pyautogui.click(1082,320)
        time.sleep(.05)
        pyautogui.moveTo(200,370)
        #pyautogui.click(1082,260)
        #pyautogui.click(1082,190)
    if(keyboard.is_pressed('q')):
        print("Total time searching was %s" % total_time_searching)
        input()
        break
    x+=1
    if x == 1999:
        print("Executed in " + str(timeit.default_timer()-start_time))
        start_time = timeit.default_timer()
        x = 0
    #print(x)

#result = subprocess.check_output(['echo | xclip -selection c -o'])
#print(result)
#os.system('source ytd.sh')
