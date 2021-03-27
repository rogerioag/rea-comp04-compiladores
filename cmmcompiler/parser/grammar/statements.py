
def p_statement_list(parser):
    """statement-list : statement-list statement
                      | empty
    """
    pass

def p_statement(parser):
    """statement : expression-stmt
                 | compound-stmt
                 | selection-stmt
                 | iteration-stmt
                 | return-stmt
    """
    pass

def p_expression(parser):
    """expression-stmt : expression SEMICOLON
                       | SEMICOLON
    """
    pass

def p_compound(parser):
    """compound-stmt : LBRACES local-declarations statement-list RBRACES"""
    pass

def p_selection(parser):
    """selection-stmt : IF LPAREN expression RPAREN statement
                      | IF LPAREN expression RPAREN statement ELSE statement
    """
    pass

def p_iteration(parser):
    """iteration-stmt : WHILE LPAREN expression RPAREN statement"""
    pass

def p_return(parser):
    """return-stmt : RETURN SEMICOLON
                   | RETURN expression SEMICOLON
    """
    pass
