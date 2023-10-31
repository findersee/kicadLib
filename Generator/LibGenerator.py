#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import sys

def main():
    """ Main entry point of the app """
    try:
        components_f = sys.argv[1]
    except:
        components_f = input("Give components txt filename: ")
    
    LibName = str(components_f.split(".")[0]) + ".kicad_sym"
    
    if len(sys.argv) == 3:
        template_f = sys.argv[2]
    else:
        template_f = 'Template.kicad_sym'
    
    try:
        template_f = open(template_f, mode='rt', encoding='utf-8')
        template = template_f.read()
        template_f.close()
    except:
        print("Error reading template")
        exit(1)
        
    Comps = "\n\r"
    with open(components_f, mode='rt', encoding='utf-8') as components:
        
        for comp in components.readlines():
            Replacet = template
            columns = comp.split("\t")
            #print(Replacet)
            Replacet = Replacet.replace("[FP]",columns[4].strip())
            Replacet = Replacet.replace("[NAME]",columns[3].strip())
            Replacet = Replacet.replace("[VALUE]",columns[0].strip())
            Replacet = Replacet.replace("[DESC]",columns[5].strip())
            Replacet = Replacet.replace("[VOLTAGE]",columns[1].strip())
            if len(columns) > 6:
                Replacet = Replacet.replace("[MAT]",columns[6].strip())
            Replacet = Replacet.replace("[SIZE]",columns[2].strip())
            Comps += Replacet + "\r\n"
            #print(Comps)
            
        
    
    Library = "(kicad_symbol_lib (version 20211014) (generator kicad_LibGenerator)"
        
    Library += Comps
    
    Library += ")"
    newDoc = open(LibName, mode='wt', encoding='utf-8')
    newDoc.write(Library)
    #template.close()
    newDoc.close()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()