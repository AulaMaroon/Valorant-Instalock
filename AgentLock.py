import time
import pyautogui
import os, ctypes


try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

if(is_admin == False):
    print('Please Run Script as Administrator')
    exit()

def wait():
    logo()
    print('1. Astra')
    print('2. Breach')
    print('3. Brimstone')
    print('4. Chamber')
    print('5. Cypher')
    print('6. Jett')
    print('7. Kayo')
    print('8. Killjoy')
    print('9. Omen')
    print('10. Pheonix')
    print('11. Raze')
    print('12. Reyna')
    print('13. Sage')
    print('14. Skye')
    print('15. Sova')
    print('16. Viper')
    print('17. Yoru')
    print()
    agent = input('Select The Agent You Want To Insta Lock : ')
    agent = int(agent)
    if agent == 1:
        Agent_Astra()
    if agent == 2:
        Agent_Breach()
    if agent == 3:
        Agent_Brimstone()
    if agent == 4:
        Agent_Chamber()
    if agent == 5:
        Agent_Cypher()
    if agent == 6:
        Agent_Jett()
    if agent == 7:
        Agent_Kayo()
    if agent == 8:
        Agent_KillJoy()
    if agent == 9:
        Agent_Omen()
    if agent == 10:
        Agent_Pheonix()
    if agent == 11:
        Agent_Raze()
    if agent == 12:
        Agent_Reyna()
    if agent == 13:
        Agent_Sage()
    if agent == 14:
        Agent_Skye()
    if agent == 15:
        Agent_Sova()
    if agent == 16:
        Agent_Viper()
    if agent == 17:
        Agent_Yoru()

def lock_in_agent():
    lockin = pyautogui.locateOnScreen('./images/lockin.png', confidence = 0.8)
    if (lockin != None):
        pyautogui.doubleClick(lockin)
        exit()

def Agent_Astra():
    waiting_agent()
    while True:
        astra = pyautogui.locateOnScreen('./images/astra.png', confidence = 0.8)
        if (astra != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(astra)
            lock_in_agent()
def Agent_Breach():
    waiting_agent()
    while True:
        breach = pyautogui.locateOnScreen('./images/breach.png', confidence = 0.8)
        if (breach != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(breach)
            lock_in_agent()
def Agent_Brimstone():
    waiting_agent()
    while True:
        brimstone = pyautogui.locateOnScreen('./images/brimstone.png', confidence = 0.8)
        if (brimstone != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(brimstone)
            lock_in_agent()
def Agent_Chamber():
    waiting_agent()
    while True:
        chamber = pyautogui.locateOnScreen('./images/chamber.png', confidence = 0.8)
        if (chamber != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(chamber)
            lock_in_agent()
def Agent_Cypher():
    waiting_agent()
    while True:
        cypher = pyautogui.locateOnScreen('./images/cypher.png', confidence = 0.8)
        if (cypher != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(cypher)
            lock_in_agent()
def Agent_Jett():
    waiting_agent()
    while True:
        jett = pyautogui.locateOnScreen('./images/jett.png', confidence = 0.8)
        if (jett != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(jett)
            lock_in_agent()
def Agent_Kayo():
    waiting_agent()
    while True:
        kayo = pyautogui.locateOnScreen('./images/kayo.png', confidence = 0.8)
        if (kayo != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(kayo)
            lock_in_agent()
def Agent_KillJoy():
    waiting_agent()
    while True:
        killjoy = pyautogui.locateOnScreen('./images/killjoy.png', confidence = 0.8)
        if (killjoy != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(killjoy)
            lock_in_agent()
def Agent_Omen():
    waiting_agent()
    while True:
        omen = pyautogui.locateOnScreen('./images/omen.png', confidence = 0.8)
        if (omen != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(omen)
            lock_in_agent()
def Agent_Pheonix():
    waiting_agent()
    while True:
        pheonix = pyautogui.locateOnScreen('./images/pheonix.png', confidence = 0.8)
        if (pheonix != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(pheonix)
            lock_in_agent()
def Agent_Raze():
    waiting_agent()
    while True:
        raze = pyautogui.locateOnScreen('./images/raze.png', confidence = 0.8)
        if (raze != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(raze)
            lock_in_agent()
def Agent_Reyna():
    waiting_agent()
    while True:
        reyna = pyautogui.locateOnScreen('./images/reyna.png', confidence = 0.8)
        if (reyna != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(reyna)
            lock_in_agent()
def Agent_Sage():
    waiting_agent()
    while True:
        sage = pyautogui.locateOnScreen('./images/sage.png', confidence = 0.8)
        if (sage != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(sage)
            lock_in_agent()
def Agent_Skye():
    waiting_agent()
    while True:
        skye = pyautogui.locateOnScreen('./images/skye.png', confidence = 0.8)
        if (skye != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(skye)
            lock_in_agent()
def Agent_Sova():
    waiting_agent()
    while True:
        sova = pyautogui.locateOnScreen('./images/sova.png', confidence = 0.8)
        if (sova != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(sova)
            lock_in_agent()
def Agent_Viper():
    waiting_agent()
    while True:
        viper = pyautogui.locateOnScreen('./images/viper.png', confidence = 0.8)
        if (viper != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(viper)
            lock_in_agent()
def Agent_Yoru():
    waiting_agent()
    while True:
        yoru = pyautogui.locateOnScreen('./images/yoru.png', confidence = 0.8)
        if (yoru != None):
            pyautogui.moveTo(960, 865)
            time.sleep(0.3)
            pyautogui.doubleClick(yoru)
            lock_in_agent()

def logo():
    os.system('cls')
    print("""                _       __  __                             
     /\        | |     |  \/  |                            
    /  \  _   _| | __ _| \  / | __ _ _ __ ___   ___  _ __  
   / /\ \| | | | |/ _` | |\/| |/ _` | '__/ _ \ / _ \| '_ \ 
  / ____ \ |_| | | (_| | |  | | (_| | | | (_) | (_) | | | |
 /_/    \_\__,_|_|\__,_|_|  |_|\__,_|_|  \___/ \___/|_| |_|
                                                           
                                                           """ )
    #print("-----------------------------------------------------------")
    return

def waiting_agent():
    os.system('cls')
    logo()
    print('Waiting On Agent Select...')
    print()
    return

wait()