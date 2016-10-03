#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler

fich = open(sys.argv[1], 'r')

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


#root-layout\twidth="248"\theight="300"\tbackground-color="blue"\region\tid="a"\ttop="20"\tleft="64"\n
