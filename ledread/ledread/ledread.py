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
            y = command.group().split(" ")[0].replace("b'","")
            if y == "turn":
                
                if command.group().split(" ")[1] == "on":
                    cmd = "turnon"
                elif command.group().split(" ")[1] == "off":
                    cmd = "turnoff"
            else:
                cmd = "switch"
            
            
            if command.group().split(" ")[2] != "through":
                x = command.group().split(" ")[4].split(",")[1].replace("\\n'","")
                coordFromY = command.group().split(" ")[2].split(",")[1]
                coordFromX = command.group().split(" ")[2].split(",")[0]
                coordToY = x
                coordToX = command.group().split(" ")[4].split(",")[0]
            else:
                x = command.group().split(" ")[3].split(",")[1].replace("\\n'","")
                coordToY = x
                coordToX = command.group().split(" ")[3].split(",")[0]
                coordFromY = command.group().split(" ")[1].split(",")[1]
                coordFromX = command.group().split(" ")[1].split(",")[0]
            coordFromX = int(coordFromX)
            coordFromY = int(coordFromY)
            coordToX = int(coordToX)
            coordToY = int(coordToY)
            if coordFromX >= 0 and coordFromY >= 0 and coordToX >= 0 and coordFromY >= 0 and coordFromX < len(n) and coordFromY < len(n) and coordToX < len(n) and coordToY < len(n):
                n = ledsol.turnOnOrOff(coordFromX,coordFromY,coordToX,coordToY,n, cmd)
    return n

"""Main module."""
