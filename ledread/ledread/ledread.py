# -*- coding: utf-8 -*-
import sys
import re
from urllib.request import urlopen
from ledsol import ledsol

def firstLine():
    f = urlopen(sys.argv[2])
    for line in f:
        command = re.match(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", str(line))
        if command == None:
            matrix = ledsol.create(int(line))
            break
    
    return matrix
            
            
            
            
def read(n):
    cmd = 0
    coordFromX = 0
    coordToX = 0
    coordFromY = 0
    coordToY = 0
    f = urlopen(sys.argv[2])
    for line in f:
        command = re.match(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", str(line))
        
        if command != None:
            y = command.group().replace("b'","")
            y = y.replace("\\n'","")
            y = y.strip()
            y = y.split(" ")
            if y[0] == "turn":
        
                if y[1] == "on":
                    cmd = "turnon"
                    y[0:2] = ""
                elif y[1] == "off":
                    cmd = "turnoff"
                    y[0:2] = ""
            elif y[0] == "switch":
                cmd = "switch"
                y[0:1] = ""
            
            y = ''.join(y).split("through")
            y = ' '.join(y)
            
            firstCoords = y.split(" ")[0].split(",")
            secondCoords = y.split(" ")[1].split(",")
            
            coordFromX = int(firstCoords[0])
            coordFromY = int(firstCoords[1])
            
            coordToX = int(secondCoords[0])
            coordToY = int(secondCoords[1])
            
    
            if coordFromX >= len(n):
                coordFromX = len(n) - 1
                
            if coordFromY >= len(n):
                coordFromY = len(n) - 1
                
            if coordToX >= len(n):
                coordToX = len(n) - 1
                
            if coordToY >= len(n):
                coordToY = len(n) - 1
                
            if coordFromX < 0:
                coordFromX = 0
                
            if coordFromY < 0:
                coordFromY = 0
                
            if coordToX < 0:
                coordToX = 0
                
            if coordToY < 0:
                coordToY = 0
            
            n = ledsol.turnOnOrOff(coordFromX,coordFromY,coordToX,coordToY,n, cmd)
    return n

"""Main module."""
