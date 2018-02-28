# -*- coding: utf-8 -*-
import sys
import re
from urllib.request import urlopen
from ledsol import ledsol

def firstLine():
    f = urlopen(sys.argv[2])
    for line in f:
        command = re.match(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", str(line))
        #if statements captures first time a line doesn't match the regex with the first line
        #always being the size of the array
        if command == None:
            #create matrix of size 'line'
            matrix = ledsol.create(int(line))
            #break from for loop so that no extra lines are read
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
        
        #if the current line matches the regex
        
        if command != None:
            #the text contains leading and trailing characters that I want to remove
            y = command.group().replace("b'","")
            y = y.replace("\\n'","")
            #sometimes the text will have leading whitespace
            y = y.strip()
            y = y.split(" ")
            if y[0] == "turn":
                #if the first word is 'turn' check the next work along
                if y[1] == "on":
                    #when a command has been taken from the line, delete the command from that line
                    #so that only the coordinates and the word 'through' remains
                    cmd = "turnon"
                    y[0:2] = ""
                elif y[1] == "off":
                    cmd = "turnoff"
                    y[0:2] = ""
            #else assume that the first word is switch
            elif y[0] == "switch":
                cmd = "switch"
                y[0:1] = ""
            
            
            #remove 'through' by splitting the line up using 'through as a delimeter
            y = ''.join(y).split("through")
            #rejoining had the advantage of removing any leading whitespace from the coordinates
            y = ' '.join(y)
            
            #first set of coordinates
            firstCoords = y.split(" ")[0].split(",")
            #second set
            secondCoords = y.split(" ")[1].split(",")
            
            
            #convert each coordinate from a string to and integer
            coordFromX = int(firstCoords[0])
            coordFromY = int(firstCoords[1])
            
            coordToX = int(secondCoords[0])
            coordToY = int(secondCoords[1])
            
            #perform checks for the size of the coordinates
    
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
            
            #turn lights on or off for current matrix
            
            n = ledsol.turnOnOrOff(coordFromX,coordFromY,coordToX,coordToY,n, cmd)
    return n

"""Main module."""
