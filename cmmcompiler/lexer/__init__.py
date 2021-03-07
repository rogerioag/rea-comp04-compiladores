__all__ = ['tokens', 'lexer', 'get_tokens']

# ------------------------------------------------------------
# tokenizer for a C subset language called C-
# ------------------------------------------------------------
import ply.lex as lex
from ply.lex import TOKEN

from .tokens import *
from .regexs import *
from .methods import *


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
