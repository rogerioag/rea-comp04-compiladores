

def p_expressions(parser):
    """expression : var ATTRIBUTION expression
                  | simple-expression
    """
    pass

def p_simple(parser):
    """simple-expression : additive-expression relop additive-expression
                         | additive-expression
    """
    pass

def p_additive(parser):
    """additive-expression : additive-expression addop term
                           | term
    """
    pass

