__all__ = ['tokens', 'TOKENS_SYMBOLS']

reserved = {
    'else': 'ELSE',
    'if': 'IF',
    'int': 'INT',
    'float': 'FLOAT',
    'return': 'RETURN',
    'void': 'VOID',
    'while': 'WHILE',
}

math_symbols = [
    'PLUS',  # +
    'MINUS',  # -
    'TIMES',  # *
    'DIVIDE'  # /
]

comparison_symbols = [
    'LESS_EQUAL',  # <=
    'LESS',  # <
    'GREATER_EQUAL',  # >=
    'GREATER',  # >
    'EQUALS',  # ==
    'DIFFERENT',  # !=
]

control_symbols = [
    'LPAREN',  # (
    'RPAREN',  # )
    'LBRACKETS',  # [
    'RBRACKETS',  # ]
    'LBRACES',  # {
    'RBRACES',  # }
    'ATTRIBUTION',  # =
    'SEMICOLON',  # ;
    'COMMA',  # ,
]

markers = [
    'ID',
    'NUMBER',
]

TOKENS_SYMBOLS = {
    'PLUS': '+',
    'MINUS': '-',
    'TIMES': '*',
    'DIVIDE': '/',
    'LESS_EQUAL': '<=',
    'LESS': '<',
    'GREATER_EQUAL': '>=',
    'GREATER': '>',
    'EQUALS': '==',
    'DIFFERENT': '!=',
    'LPAREN': '(',
    'RPAREN': ')',
    'LBRACKETS': '[',
    'RBRACKETS': ']',
    'LBRACES': '{',
    'RBRACES': '}',
    'ATTRIBUTION': '=',
    'SEMICOLON': ';',
    'COMMA': ',',
    'ELSE': 'else',
    'IF': 'if',
    'INT': 'int',
    'FLOAT': 'float',
    'RETURN': 'return',
    'VOID': 'void',
    'WHILE': 'while',
}

tokens = markers + math_symbols + comparison_symbols + \
    control_symbols + list(reserved.values())
