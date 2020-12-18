import pyautogui
def UP():
    pyautogui.keyDown("up")
    pyautogui.keyUp("up")
    pyautogui.keyUp("down")
def Down():    
    pyautogui.keyDown("down")
    pyautogui.keyUp("down")
    pyautogui.keyUp("up")
def no_key():
    pass