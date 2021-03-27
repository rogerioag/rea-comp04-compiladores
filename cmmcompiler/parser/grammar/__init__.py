
from .declarations import *
from .expressions import *
from .operations import *
from .params import *
from .types import *
from .statements import *

def p_program(parser):
    """program : declaration-list"""
    pass

def p_var(parser):
    """var : ID
           | ID LBRACKETS expression RBRACKETS
    """
    pass


def p_term(parser):
    """term : mulop factor
            | factor
    """
    pass

def p_factor(parser):
    """factor : LPAREN expression RPAREN
              | var
              | call
              | NUMBER
    """
    pass

def p_call(parser):
    """call : ID LPAREN args RPAREN"""
    pass

def p_args(parser):
    """args : arg-list
            | empty
    """
    pass

def p_arg_list(parser):
    """arg-list : arg-list SEMICOLON expression
                | expression
    """
    pass

def p_empty(parser):
    """empty :"""
    pass

def p_error(parser):
    pass