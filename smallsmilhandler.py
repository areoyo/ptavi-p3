#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class smallSMILHandler(ContentHandler):

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.root_layout = {}
        self.region = {}
        self.img = {}
        self.audio = {}
        self.textstream = {}
        self.misdatos = []
       
    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.root_layout = {'width': str(attrs.get('width',"")), 
                                'height': str(attrs.get('height',"")), 
                                'background-color': str(attrs.get('background-color',""))}
                              
            self.misdatos.append(self.root_layout)
            self.root_layout = {}

        elif name == 'region':
            self.region = {'id': str(attrs.get('id',"")),
                           'top': str(attrs.get('top',"")),
                           'bottom': str(attrs.get('bottom',"")),
                           'left': str(attrs.get('left',"")),
                           'right': str(attrs.get('right',""))}

            self.misdatos.append(self.region)
            self.region = {}
            
        elif name == 'img':     
            self.img = {'src': str(attrs.get('src',"")),
                        'region': str(attrs.get('region',"")),
                        'begin': str(attrs.get('begin',"")),
                        'dur': str(attrs.get('dur',""))}

            self.misdatos.append(self.img)
            self.img = {}
            
        elif name == 'audio':
            self.audio = {'src': str(attrs.get('src',"")),
                          'begin': str(attrs.get('begin',"")),
                          'dur': str(attrs.get('dur', ""))}

            self.misdatos.append(self.audio)
            self.audio = {}
            
        elif name == 'textstream':
            self.textstream = {'src': str(attrs.get('src',"")),
                               'region': str(attrs.get('region',""))}

            self.misdatos.append(self.textstream)
            self.textstream = {}
            
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

        
