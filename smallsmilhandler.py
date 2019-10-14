#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista = []
        self.elemDict = {
                        "root-layout": ["width", "height", "background-color"],
                        "region": ["id", "top", "left", "right"],
                        "img": ["src", "region", "begin", "dur"],
                        "audio": ["src", "begin", "dur"],
                        "textstream": ["src", "region"]
                        }

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name in self.elemDict:
            # De esta manera tomamos los valores de los atributos
            dicc = {}
            dicc['etiqueta'] = name
            for atributo in self.elemDict[name]:
                dicc[atributo] = attrs.get(atributo, "")
            self.lista.append(dicc)

    def get_tags(self):
        return(self.lista)


if __name__ == "__main__":
    """
    Programa principal
    """
    ficherosmil = 'karaoke.smil'
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(ficherosmil))
    lista = cHandler.get_tags()
    print(lista)
