__all__ = ['parser']

import ply.yacc as yacc
from lexer import tokens
from .grammar import *

# parser = yacc.yacc(start='program')
parser = yacc.yacc(method="LALR", optimize=True, start='program', debug=True,
                   debuglog=log, write_tables=False, tabmodule='cmm_parser_tab')