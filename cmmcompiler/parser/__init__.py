__all__ = ['parser']

import ply.yacc as yacc
from .grammar import *
from lexer import tokens


parser = yacc.yacc(start='program', tracking=True)