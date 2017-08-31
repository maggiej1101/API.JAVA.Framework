import ctypes
import time
import string, os, sys
from os import path
	
# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKeyBoardKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def PressKeyBoardKeyEnter():
    PressKeyBoardKey(0x0D) #Enter
    time.sleep(1)

def ReleaseKeyBoardKeyEnter():
    ReleaseKey(0x0D) #Enter
    time.sleep(1)

def PressKeyBoardKeyDownArrow():
    PressKeyBoardKey(0x028) #Enter
    time.sleep(1)

def PressKeyBoardKeyUpArrow():
    PressKeyBoardKey(0x026) #Enter
    time.sleep(1)

def PressKeyBoardKeyTab():
    PressKeyBoardKey(0x012) #Enter
    time.sleep(2)
	
def PressKeyBoardKeyPageUp():
	PressKeyBoardKey(0x021) #Enter
	time.sleep(1)
	
def PressKeyBoardKeyPageDown():
	PressKeyBoardKey(0x022) #Enter
	time.sleep(1)
	
def PressKeyNumPadKeyHyphen():
	PressKeyBoardKey(0x6D) #Num pad hyphen
	time.sleep(1)
	
def PressKeyNumPadKeyPlus():
	PressKeyBoardKey(0x6B) #Num pad plus
	time.sleep(1)
	
def PressKeyBoardKeyPlus():
	PressKeyBoardKey(0xA1)
	PressKeyBoardKey(0xBB) #keyboard plus 
	ReleaseKey(0xA1)
	time.sleep(1)	

def PressKeyBoardKeyMinus():
	PressKeyBoardKey(0xBD) #keyboard minus/hyphen
	time.sleep(1)	
	
def PressKeyBoardKeyOpenParenthesis():
	PressKeyBoardKey(0xA1)
	PressKeyBoardKey(0x39) #keyboard Open Parenthesis 
	ReleaseKey(0xA1)
	time.sleep(1)

def PressKeyBoardKeyCloseParenthesis():
	PressKeyBoardKey(0xA1)
	PressKeyBoardKey(0x30) #keyboard Close Parenthesis 
	ReleaseKey(0xA1)
	time.sleep(1)

def PressKeyBoardKeyALTF4():
	PressKeyBoardKey(0xA4)
	PressKeyBoardKey(0x73) #keyboard Close Parenthesis 
	ReleaseKey(0xA4)
	time.sleep(1)

def AltTab():
    '''
    Press Alt+Tab and hold Alt key for 2 seconds in order to see the overlay
    '''

    PressKey(0x012) #Alt
    PressKey(0x09) #Tab
    ReleaseKey(0x09) #~Tab

    time.sleep(2)       
    ReleaseKey(0x012) #~Alt
	
def PressKeyBoardKeyF4():
    PressKeyBoardKey(0x73) #F4
    time.sleep(1)
	
def PressKeyBoardKeyF10():
    PressKeyBoardKey(0x79) #F10
    time.sleep(1)
	
def PressKeyBoardKeyF1():
    PressKeyBoardKey(0x70) #F1
    time.sleep(1)
	
def PressKeyBoardKeyF2():
    PressKeyBoardKey(0x71) #F2
    time.sleep(1)
	
def PressKeyBoardKeyF3():
    PressKeyBoardKey(0x72) #F3
    time.sleep(1)
	
def PressKeyBoardKeyF5():
    PressKeyBoardKey(0x74) #F5
    time.sleep(1)
	
def PressKeyBoardKeyF6():
    PressKeyBoardKey(0x75) #F6
    time.sleep(1)
	
def PressKeyBoardKeyF7():
    PressKeyBoardKey(0x76) #F7
    time.sleep(1)
	
def PressKeyBoardKeyF8():
    PressKeyBoardKey(0x77) #F8
    time.sleep(1)
	
def PressKeyBoardKeyF9():
    PressKeyBoardKey(0x78) #F9
    time.sleep(1)

def PressKeyBoardKeyF11():
    PressKeyBoardKey(0x7A) #F11
    time.sleep(1)

def PressKeyBoardKeyF12():
    PressKeyBoardKey(0x7B) #F12
    time.sleep(1)

def PressKeyBoardKeyF13():
    PressKeyBoardKey(0x7C) #F13
    time.sleep(1)
	
def PressKeyBoardKeyF14():
    PressKeyBoardKey(0x7D) #F14
    time.sleep(1)
def PressKeyBoardKeyPageUp():
                PressKeyBoardKey(0x021) #Page Up
                time.sleep(1)

def ConvertStringToHexKeyCode(input_string):    
    return (":".join("{:02x}".format(ord(c)) for c in input_string.upper()))


if __name__ =="__main__":

     AltTab()
