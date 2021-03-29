from lexer import TOKENS_SYMBOLS
from tree import TreeNode

def p_type_specifier(parser):
    """type-specifier : int
                      | void
    """
    parser[0] = TreeNode(id='TYPE_SPECIFIER')
    [node, type_node] = parser

    node.insert_node(type_node)
    pass

def p_void(parser):
    """void : VOID """
    [_, raw] = parser
    parser[0] = TreeNode(id='VOID', raw=raw)
    pass

def p_int(parser):
    """int : INT """
    [_, raw] = parser
    parser[0] = TreeNode(id='INT', raw=raw)
    pass