#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
import json

try:
    fich = open(sys.argv[1], 'r')
except IndexError:
    sys.exit("Usage: python3 karaoke.py file.smil")
    
if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    kHandler = smallsmilhandler.smallSMILHandler()
    parser.setContentHandler(kHandler)
    parser.parse(fich)
    mis_datos = kHandler.get_tags()

    for atributos in mis_datos:
        tag = atributos['tag']
        del atributos['tag']
        line = str(tag+'\t')
        for atribute in atributos:
            line = line+atribute+"="+atributos[atribute]+'\t'
        print(line)
