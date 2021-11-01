__all__ = ['p_relational', 'p_addition', 'p_multiplication']

from lexer import TOKENS_SYMBOLS
from tree import TreeNode

def get_token_by_raw(raw):
    
    for (token, value) in TOKENS_SYMBOLS.items():
        if value == raw:
            return token
        pass

    return None

def p_relational(parser):
    """relop : LESS_EQUAL
             | LESS
             | GREATER
             | GREATER_EQUAL
             | EQUALS
             | DIFFERENT
    """
    [_, raw] = parser
    parser[0] = TreeNode(id=get_token_by_raw(raw))
    parser[0].insert_node(TreeNode(raw=raw))
    pass

def p_addition(parser):
    """addop : PLUS
             | MINUS
    """
    [_, raw] = parser
    parser[0] = TreeNode(id=get_token_by_raw(raw))
    parser[0].insert_node(TreeNode(raw=raw))
    pass

def p_multiplication(parser):
    """mulop : TIMES
             | DIVIDE
    """
    [_, raw] = parser
    parser[0] = TreeNode(id=get_token_by_raw(raw))
    parser[0].insert_node(TreeNode(raw=raw))
    pass
