__all__ = ['tokens', 'lexer', 'get_tokens', 'TOKENS_SYMBOLS', 'number_regex']

# ------------------------------------------------------------
# tokenizer for a C subset language called C-
# ------------------------------------------------------------
import ply.lex as lex
from ply.lex import TOKEN

from .tokens import *
from .regexs import *
from .methods import *

from .regexs import t_NUMBER as number_regex

from sys import argv, exit

import logging

logging.basicConfig(
     level = logging.DEBUG,
     filename = "parser.log",
     filemode = "w",
     format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

def get_tokens(input):
    lexer = lex.lex()
    lexer.input(input)

    tokens = []
    token = lexer.token()
    while token:
        tokens.append(token)
        token = lexer.token()
        pass

    return tokens
    pass


lexer = lex.lex()
