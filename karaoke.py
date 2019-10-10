#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:43:08 2019

@author: ana
"""

import smallsmilhandler
import sys


       
        
if __name__ == "__main__":
    if len(sys.argv) != 2 :
        sys.exit("Usage: python3 karaoke.py file.smil")
        
    fichero = sys.argv[1]
    comprobacion = fichero.split('.')
    
    if comprobacion[1] != ('smil'):
        sys.exit("Introducido un fichero distinto a .smil")
    

    smallsmilhandler.manejador(fichero)
    
    
    
 
    