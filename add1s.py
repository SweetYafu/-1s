# -*- coding:UTF-8 -*-
__author__ = "Sweet Yafu"

'''
Add 1s to HIM
'''

import os, time, commands

windowSize = (56, 44) # row, column

def writeBuffer(line, col, _str):
    buffer = [[" " for i in range(windowSize[0])] for j in range(windowSize[1])]
    for index, i in enumerate(_str):
        buffer[line][col+index] = i
    return buffer


row = 0
col = 0

while(True):
    os.system("clear")
    _buf = writeBuffer(row, col, "FUCK YOU")
    for i in _buf:
        print  "".join(i)
    if(row < windowSize[0]-40):
        row += 1
    else:
        row -= 1
    if(col < windowSize[1]-9):
        col += 1
    else:
        col -= 1

    time.sleep(0.2)



