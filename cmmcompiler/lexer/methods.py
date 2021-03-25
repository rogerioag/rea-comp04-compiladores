from ply.lex import TOKEN

from .regexs import id_regex, comment_regex
from .tokens import reserved

t_ignore = ' \t'

@TOKEN(id_regex)
def t_ID(t):
    t.type = reserved.get(t.value, 'ID')
    return t

@TOKEN(comment_regex)
def t_ignore_COMMENT(r):
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Símbolo não definido pela linguagem '%s'" % t.value[0])
    t.lexer.skip(1)
