import os
import time
import re
from pynput import mouse
from pynput.keyboard import Key, Listener

from pynput import keyboard

def on_press(key):
    print('{0} pressed'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False
with Listener(on_press=on_press) as listener:
    listener.join()

def  on_click(x, y, button, pressed):
    f=open('maniac1.txt','a')
    if button == mouse.Button.left:
        print ('Left')
        #f.write('left\n')
    if button == mouse.Button.right:
        print ('right')
        #f.write('right\n')
    if button == mouse.Button.middle:
        print ('middle')
    #f.write('middle\n')

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

print(on_press)
print(on_click)
