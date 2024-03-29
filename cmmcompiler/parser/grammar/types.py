from lexer import TOKENS_SYMBOLS
from tree import TreeNode

def p_type_specifier(parser):
    """type-specifier : int
                      | void
    """
    parser[0] = TreeNode(id='type-specifier')
    [node, type_node] = parser

    node.insert_node(type_node)
    pass

def p_void(parser):
    """void : VOID """
    #[_, raw] = parser
    #parser[0] = TreeNode(id='VOID', raw=raw)
    parser[0] = TreeNode(id='VOID')
    [node, lexeme] = parser

    node.insert_node(TreeNode(raw=lexeme))
    pass

def p_int(parser):
    """int : INT """
    #[_, raw] = parser
    #parser[0] = TreeNode(id='INT', raw=raw)

    parser[0] = TreeNode(id='INT')
    [node, lexeme] = parser

    node.insert_node(TreeNode(raw=lexeme))

    pass