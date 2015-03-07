'''
Created on 27/11/2014

@author: Yuri A. Nascimento
'''
from LSystem import LSystem
""" Referências:
[1] PRUSINKIEWICZ, Przemyslaw e LINDENMAYER, Aristid (1990): The
Algorithmic Beauty of Plants. Springer-Verlag. """

#[1] - Pág: 08, Fig: 1.6
KOCH = LSystem('F-F-F-F', 'F->F-F+F+FF-F-F+F')
KOCH_ANGLE = 90

#[1] - Pág: 25, Fig: 1.24(c)
PLANT = LSystem('F', 'F->FF-[-F+F+F]+[+F-F-F]')
PLANT_ANGLE = 22.5

#[1] - Pág: 2, Fig: 1.1
SNOWFLAKE = LSystem('F--F--F', 'F->F+F--F+F')
SNOWFLAKE_ANGLE = 60

#[1] - Pág: 11, Fig: 1.10(a)
DRAGON = LSystem('Fl', 'l->l+rF+, r->-Fl-r')
DRAGON_ANGLE = 90

#[1] - Pág: 17, Fig: 1.16(a)
FASS = LSystem('-L', 'L→LF+RFR+FL-F-LFLFL-FRFR+, R→-LFLF+RFRFR+F+RF-LFL-FR')
FASS_ANGLE = 90
