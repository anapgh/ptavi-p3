#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:43:08 2019

@author: ana
"""

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 :
        sys.exit("Usage: python3 karaoke.py file.smil")
        
    ficherosmil = sys.argv[1]
    
    fichero = open(ficherosmil, 'r')
    datos = fichero.read()
    print(datos)