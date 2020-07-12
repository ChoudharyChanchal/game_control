#This code is borrowed form Wassim Gharbi https://github.com/wassgha/pygta-mac/blob/master/directkeys.py

# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html


#!/usr/bin/env python

import time
from Quartz.CoreGraphics import CGEventCreateKeyboardEvent
from Quartz.CoreGraphics import CGEventPost

# Python releases things automatically, using CFRelease will result in a scary error
#from Quartz.CoreGraphics import CFRelease

from Quartz.CoreGraphics import kCGHIDEventTap

# From http://stackoverflow.com/questions/281133/controlling-the-mouse-from-python-in-os-x
# and from https://developer.apple.com/library/mac/documentation/Carbon/Reference/QuartzEventServicesRef/index.html#//apple_ref/c/func/CGEventCreateKeyboardEvent

W = 0x0D
A = 0x00
S = 0x01
D = 0x02

def KeyDown(k):
    keyCode, shiftKey = toKeyCode(k)

    time.sleep(0.0001)

    if shiftKey:
        CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, 0x38, True))
        time.sleep(0.0001)

    CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, keyCode, True))
    time.sleep(0.0001)

    if shiftKey:
        CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, 0x38, False))
        time.sleep(0.0001)

def KeyUp(k):
    keyCode, shiftKey = toKeyCode(k)

    time.sleep(0.0001)

    CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, keyCode, False))
    time.sleep(0.0001)

def PressKey(keyCode):

    time.sleep(0.0001)

    CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, keyCode, True))
    time.sleep(0.0001)

def ReleaseKey(keyCode):

    time.sleep(0.0001)

    CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, keyCode, False))
    time.sleep(0.0001)


# From http://stackoverflow.com/questions/3202629/where-can-i-find-a-list-of-mac-virtual-key-codes

def toKeyCode(c):
    shiftKey = False
    # Letter
    if c.isalpha():
        if not c.islower():
            shiftKey = True
            c = c.lower()

    if c in shiftChars:
        shiftKey = True
        c = shiftChars[c]
    if c in keyCodeMap:
        keyCode = keyCodeMap[c]
    else:
        keyCode = ord(c)
    return keyCode, shiftKey

shiftChars = {
    '~': '`',
    '!': '1',
    '@': '2',
    '#': '3',
    '$': '4',
    '%': '5',
    '^': '6',
    '&': '7',
    '*': '8',
    '(': '9',
    ')': '0',
    '_': '-',
    '+': '=',
    '{': '[',
    '}': ']',
    '|': '\\',
    ':': ';',
    '"': '\'',
    '<': ',',
    '>': '.',
    '?': '/'
}


keyCodeMap = {
    'a'                 : 0x00,
    's'                 : 0x01,
    'd'                 : 0x02,
    'f'                 : 0x03,
    'h'                 : 0x04,
    'g'                 : 0x05,
    'z'                 : 0x06,
    'x'                 : 0x07,
    'c'                 : 0x08,
    'v'                 : 0x09,
    'b'                 : 0x0B,
    'q'                 : 0x0C,
    'w'                 : 0x0D,
    'e'                 : 0x0E,
    'r'                 : 0x0F,
    'y'                 : 0x10,
    't'                 : 0x11,
    '1'                 : 0x12,
    '2'                 : 0x13,
    '3'                 : 0x14,
    '4'                 : 0x15,
    '6'                 : 0x16,
    '5'                 : 0x17,
    '='                 : 0x18,
    '9'                 : 0x19,
    '7'                 : 0x1A,
    '-'                 : 0x1B,
    '8'                 : 0x1C,
    '0'                 : 0x1D,
    ']'                 : 0x1E,
    'o'                 : 0x1F,
    'u'                 : 0x20,
    '['                 : 0x21,
    'i'                 : 0x22,
    'p'                 : 0x23,
    'l'                 : 0x25,
    'j'                 : 0x26,
    '\''                : 0x27,
    'k'                 : 0x28,
    ';'                 : 0x29,
    '\\'                : 0x2A,
    ','                 : 0x2B,
    '/'                 : 0x2C,
    'n'                 : 0x2D,
    'm'                 : 0x2E,
    '.'                 : 0x2F,
    '`'                 : 0x32,
    'k.'                : 0x41,
    'k*'                : 0x43,
    'k+'                : 0x45,
    'kclear'            : 0x47,
    'k/'                : 0x4B,
    'k\n'               : 0x4C,
    'k-'                : 0x4E,
    'k='                : 0x51,
    'k0'                : 0x52,
    'k1'                : 0x53,
    'k2'                : 0x54,
    'k3'                : 0x55,
    'k4'                : 0x56,
    'k5'                : 0x57,
    'k6'                : 0x58,
    'k7'                : 0x59,
    'k8'                : 0x5B,
    'k9'                : 0x5C,

    # keycodes for keys that are independent of keyboard layout
    '\n'                : 0x24,
    '\t'                : 0x30,
    ' '                 : 0x31,
    'del'               : 0x33,
    'delete'            : 0x33,
    'esc'               : 0x35,
    'escape'            : 0x35,
    'cmd'               : 0x37,
    'command'           : 0x37,
    'shift'             : 0x38,
    'caps lock'         : 0x39,
    'option'            : 0x3A,
    'ctrl'              : 0x3B,
    'control'           : 0x3B,
    'right shift'       : 0x3C,
    'rshift'            : 0x3C,
    'right option'      : 0x3D,
    'roption'           : 0x3D,
    'right control'     : 0x3E,
    'rcontrol'          : 0x3E,
    'fun'               : 0x3F,
    'function'          : 0x3F,
    'f17'               : 0x40,
    'volume up'         : 0x48,
    'volume down'       : 0x49,
    'mute'              : 0x4A,
    'f18'               : 0x4F,
    'f19'               : 0x50,
    'f20'               : 0x5A,
    'f5'                : 0x60,
    'f6'                : 0x61,
    'f7'                : 0x62,
    'f3'                : 0x63,
    'f8'                : 0x64,
    'f9'                : 0x65,
    'f11'               : 0x67,
    'f13'               : 0x69,
    'f16'               : 0x6A,
    'f14'               : 0x6B,
    'f10'               : 0x6D,
    'f12'               : 0x6F,
    'f15'               : 0x71,
    'help'              : 0x72,
    'home'              : 0x73,
    'pgup'              : 0x74,
    'page up'           : 0x74,
    'forward delete'    : 0x75,
    'f4'                : 0x76,
    'end'               : 0x77,
    'f2'                : 0x78,
    'page down'         : 0x79,
    'pgdn'              : 0x79,
    'f1'                : 0x7A,
    'left'              : 0x7B,
    'right'             : 0x7C,
    'down'              : 0x7D,
    'up'                : 0x7E
}

if __name__ == '__main__':
    PressKey(0x0D)
    time.sleep(1)
    ReleaseKey(0x0D)
    time.sleep(1)
    
    