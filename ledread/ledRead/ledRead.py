# -*- coding: utf-8 -*-
import sys


def read():
    file_handle = open(sys.argv[0], 'r')
    for i in file_handle:
        print(i)
    return file_handle




"""Main module."""
