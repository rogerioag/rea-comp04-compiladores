__all__ = ['parser']

import ply.yacc as yacc
from .grammar import *
from lexer import tokens


# parser = yacc.yacc(start='program')
parser = yacc.yacc(method="LALR", optimize=True, start='program', debug=True,
                   debuglog=log, write_tables=False, tabmodule='cmm_parser_tab')