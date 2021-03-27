

def p_params(parser):
    """params : param-list
              | void
    """
    pass

def p_param_list(parser):
    """param-list : param-list COMMA param
                  | param
    """
    pass

def p_param(parser):
    """param : type-specifier ID
             | type-specifier ID LBRACKETS RBRACKETS
    """
    pass
