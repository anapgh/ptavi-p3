#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:06:08 2019

@author: ana
"""
from xml.sax import make_parser
import smallsmilhandler
import sys
import json
import urllib.request


class KaraokeLocal():
    """docstring for ."""

    def __init__(self, fichero_smil):
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        try:
            parser.parse(open(fichero_smil))
        except FileNotFoundError:
            sys.exit("File not exist")
        self.lista = cHandler.get_tags()

    def __str__(self):
        salida = ''
        for elemDict in self.lista:
            atributos = ""
            for atributo in elemDict.items():
                clave, valor = atributo
                if clave == 'etiqueta':
                    etiqueta = valor
                else:
                    atributos += '\t' + clave + '="' + valor + '"'

            salida += etiqueta + atributos + "\n"
        return(salida)

    def to_json(self, fichero_smil, fichero_json=""):
        if not fichero_json:
            fichero_json = fichero_smil.replace(".smil", ".json")
        with open(fichero_json, "w") as outfile:
            json.dump(self.lista, outfile, indent=1)

    def do_local(self):
        for elemDict in self.lista:
            atributos = ''
            for atributo in elemDict.items():
                clave, valor = atributo
                if clave == 'src':
                    if valor.startswith("http://"):
                        urllib.request.urlretrieve(valor)
                        print("Descargando ... " + valor)
                        valor = valor.split('/')[-1]
                        elemDict[clave] = valor


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")

    fichero_smil = sys.argv[1]
    comprobacion = fichero_smil.split('.')
    try:
        if comprobacion[1] != ('smil'):
            sys.exit("Introducido un fichero distinto a .smil")
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

    fichero_json = 'local.json'
    c = KaraokeLocal(fichero_smil)
    print(c)
    c.to_json(fichero_smil)
    c.do_local()
    c.to_json(fichero_json)
    print(c)
