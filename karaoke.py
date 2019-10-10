#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:43:08 2019

@author: ana
"""
from xml.sax import make_parser
import smallsmilhandler
import sys

 
if __name__ == "__main__":
    try:
        if len(sys.argv) != 2 :
            sys.exit("Usage: python3 karaoke.py file.smil")
        
        fichero = sys.argv[1]
        comprobacion = fichero.split('.')
        
        if comprobacion[1] != ('smil'):
            sys.exit("Introducido un fichero distinto a .smil")
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")
            
        
    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(fichero))
    lista = cHandler.get_tags()
    for elementDict in lista:
        atributos = ''
        for atributo in elementDict.items():
           clave,valor = atributo
           if clave == 'etiqueta':
               etiqueta = valor
           else:
               atributos += ("\\" +'t'+ clave + '="' + valor + '"')
        print(etiqueta + atributos + "\\n")