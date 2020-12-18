import win32api as wapi
import win32con as wcon
def key_check():
    keys=[]
    if wapi.GetAsyncKeyState(wcon.VK_UP):
        keys.append('up')
    if wapi.GetAsyncKeyState(wcon.VK_DOWN):
        keys.append('down')
    return keys 
def keys_to_output(keys):
    output = [0,0,0]
    if 'up' in keys:
        output[0] = 1
    elif 'down' in keys:
        output[2] = 1
    else:
        output[1] = 1
    print("output is :",output)    
    return output