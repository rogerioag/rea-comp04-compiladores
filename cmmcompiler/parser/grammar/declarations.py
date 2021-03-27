


def p_declaration_list(parser):
    """declaration-list : declaration-list declaration
                        | declaration
    """
    pass


def p_declaration(parser):
    """declaration : var-declaration
                   | fun-declaration
    """
    pass

def p_var_declaration(parser):
    """var-declaration : type-specifier ID SEMICOLON
                       | type-specifier ID LBRACKETS NUMBER RBRACKETS
    """
    pass

def p_fun_declaration(parser):
    """fun-declaration : type-specifier ID LPAREN params RPAREN compound-stmt"""
    pass

def p_local_declarations(parser):
    """local-declarations : local-declarations var-declaration
                          | empty
    """
    pass
