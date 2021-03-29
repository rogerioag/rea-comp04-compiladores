from lexer import TOKENS_SYMBOLS
from tree import TreeNode

def p_expressions(parser):
    """expression : var ATTRIBUTION expression
                  | simple-expression
    """
    parser[0] = TreeNode(id='EXPRESSION')

    [node, subtree] = parser[:2]

    node.insert_node(subtree)
    if len(parser) > 2:
        [_, exp] = parser[2:4]
        node.insert_node(TreeNode(id='ATTRIBUTION', raw=TOKENS_SYMBOLS.get('ATTRIBUTION')))
        node.insert_node(exp)
        pass
    pass

def p_simple(parser):
    """simple-expression : additive-expression relop additive-expression
                         | additive-expression
    """
    parser[0] = TreeNode(id='SIMPLE_EXPRESSION')

    [node, add] = parser[:2]

    node.insert_node(add)
    if len(parser) > 2:
        [relop, addi] = parser[2:4]
        node.insert_node(relop)
        node.insert_node(addi)
        pass
    pass

def p_additive(parser):
    """additive-expression : additive-expression addop term
                           | term
    """
    parser[0] = TreeNode(id='ADDITIVE_EXPRESSION')

    [node, subtree] = parser[:2]

    node.insert_node(subtree)
    if len(parser) > 2:
        [addop, term] = parser[2:4]
        node.insert_node(addop)
        node.insert_node(term)
        pass
    pass

