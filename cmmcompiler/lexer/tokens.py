__all__ = ['tokens']

reserved = {
    'else': 'ELSE',
    'if': 'IF',
    'int': 'INT',
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

tokens = markers + math_symbols + comparison_symbols + \
    control_symbols + list(reserved.values())
