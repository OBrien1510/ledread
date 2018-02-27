# -*- coding: utf-8 -*-
import sys
import re


def read():
    
    regex = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
    with open(sys.argv[0], 'r') as f:
        for line in f:
            result = regex.search(line)
            print(result.group())




"""Main module."""
