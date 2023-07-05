import pyautogui
import time
import yaml

def Teraterm():
    pyautogui.press('win')
    time.sleep(3)
    pyautogui.typewrite('teraterm')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('winleft','up')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

def Aampcli():
    pyautogui.typewrite('cd /usr/lib')
    pyautogui.press('enter')
    pyautogui.typewrite('./aamp-cli')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite('1005')
    pyautogui.press('enter')
    time.sleep(15)

def seekFW():
    pyautogui.press('enter')
    pyautogui.typewrite('seek 120')
    pyautogui.press('enter')
    time.sleep(10)

def seekRW():
    pyautogui.press('enter')
    pyautogui.typewrite('seek 30')
    pyautogui.press('enter')
    time.sleep(10)

def pause():
    # time.sleep(10)
    pyautogui.press('enter')
    pyautogui.typewrite('pause')
    pyautogui.press('enter')
    time.sleep(10)

def schedule_pause_verification():
    # time.sleep(42)
    pyautogui.press('enter')
    pyautogui.typewrite('pause 60')
    pyautogui.press('enter')
    time.sleep(30)
    
def play():
    pyautogui.press('enter')
    pyautogui.typewrite('play')
    pyautogui.press('enter')
    time.sleep(10)
    
def slow_motion():
    # Aampcli()
    pyautogui.press('enter')
    pyautogui.typewrite('slow')
    pyautogui.press('enter')
    time.sleep(10)

def Stop():
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.typewrite('stop')
    pyautogui.press('enter')
    time.sleep(15)

def Streamfailure():
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.typewrite('1168')
    pyautogui.press('enter')
    time.sleep(20)
    
def live_profile_verification():
    with open(r'C:\Users\40030149\OneDrive - LTTS\Desktop\FOXTEL\config.yaml') as file:
        databaseConfig = yaml.safe_load(file)
        # print(databaseConfig)
        url = databaseConfig['URL']
        print("url ", url)
        # pyautogui.press('enter')
        pyautogui.typewrite(url[3])
        time.sleep(3)
        pyautogui.typewrite('live')
        time.sleep(3)
        pyautogui.press('enter')
        


def Segment_number_verification():
    Aampcli()
    pyautogui.typewrite('get 16')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite('set 16 507246 ')
    pyautogui.press('enter')
    pyautogui.typewrite('underflow')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite('retune')
    pyautogui.press('enter')
    time.sleep(2)
    
def Single_period():
    Aampcli()
    pyautogui.typewrite('get 34')
    pyautogui.press('enter')
    pyautogui.typewrite('set 16 507246 ')
    pyautogui.press('enter')
    pyautogui.typewrite('underflow')
    pyautogui.press('enter')
    pyautogui.typewrite('retune')
    pyautogui.press('enter')
    pyautogui.hotkey('alt','f4')
    time.sleep(2)
    pyautogui.press('enter')

def Stream_playback():
    pyautogui.press('enter')
    pyautogui.typewrite('1000')
    pyautogui.press('enter')

# def Stop():
#     pyautogui.press('enter')
#     pyautogui.typewrite('stop')
#     pyautogui.press('enter')
    
def Stream_Play():
    with open(r'D:\Automation_POC\config.yaml') as file:
        databaseConfig = yaml.safe_load(file)
        # print(databaseConfig)
        url = databaseConfig['URL']
        print("url ", url)
        pyautogui.typewrite(url[0])
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1)