#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class smallSMILHandler(ContentHandler):

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.misdatos = []
        self.atributos = {'root-layout': ['width', 'height', 'background-color'],
                          'region': ['id', 'top', 'bottom', 'left', 'right'],
                          'img': ['src', 'region','begin', 'dur'],
                          'audio': ['src', 'begin', 'dur'],
                          'textstream': ['src', 'region']}
        self.etiquetas = ['root-layout', 'region', 'img', 'audio', 'textstream']


    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        dicc = {}        
        if name in self.etiquetas:
            dicc = {'tag': name}
            for atributo in self.atributos[name]:
                dicc[atributo] = str(attrs.get(atributo,"")) 
            self.misdatos.append(dicc)

    def get_tags (self):
        """
        Método que se llama para guardar la lista de datos
        """
        return self.misdatos
        
if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    kHandler = smallSMILHandler()
    parser.setContentHandler(kHandler)
    parser.parse(open('karaoke.smil'))
    mis_datos = kHandler.get_tags()

    for atribute in mis_datos:
        print(atribute)

        
