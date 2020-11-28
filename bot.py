from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api,win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('e')== False :
    if keyboard.is_pressed('a')==True :
        continue
    if pyautogui.pixel(369,580)[0] == 0:
        click(369,580)
    if pyautogui.pixel(457,580)[0] == 0:
        click(457,580)
    if pyautogui.pixel(538,580)[0] == 0:
        click(538,580)
    if pyautogui.pixel(638,580)[0] == 0:
        click(638,580)
