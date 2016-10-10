#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class smallSMILHandler(ContentHandler):

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.misdatos = []
        self.attrs = {'root-layout': ['width', 'height', 'background-color'],
                          'region': ['id', 'top', 'bottom', 'left', 'right'],
                          'img': ['src', 'region', 'begin', 'dur'],
                          'audio': ['src', 'begin', 'dur'],
                          'textstream': ['src', 'region']}

    def startElement(self, name, atributes):
        """
        Método que se llama cuando se abre una etiqueta
        """
        dicc = {}
        if name in self.attrs:
            dicc = {'tag': name}
            for atributo in self.attrs[name]:
                dicc[atributo] = str(atributes.get(atributo, "")) 
            self.misdatos.append(dicc)

    def get_tags(self):
        """
        Método que se llama para guardar la lista de datos
        """
        return self.misdatos
