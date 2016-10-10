#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
import json
import urllib.request
    
def file_JSON(data):
    fichjson = open(sys.argv[1].split('.')[0]+'.json','w')
    fichjson.write(json.dumps(data))
    fichjson.close()
    
    
if __name__ == "__main__":
    """
    Programa principal
    """
    try:
        fich = open(sys.argv[1], 'r')
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
        
    parser = make_parser()
    kHandler = smallsmilhandler.smallSMILHandler()
    parser.setContentHandler(kHandler)
    parser.parse(fich)
    mis_datos = kHandler.get_tags()
    
    file_JSON(mis_datos)

    for atributos in mis_datos:
        tag = atributos['tag']
        del atributos['tag']
        line = str(tag+'\t')
        
        for atribute in atributos:
            if atributos[atribute][:7] == 'http://':
                print('DESCARGO')
                name = atributos[atribute].split('/')[-1]
                url = urllib.request.urlretrieve(atributos[atribute], name )
                atributos[atribute] = name
        
            line = line+atribute+"="+atributos[atribute]+'\t'
        print(line)
