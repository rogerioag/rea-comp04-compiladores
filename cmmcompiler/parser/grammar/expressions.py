from lexer import TOKENS_SYMBOLS
from tree import TreeNode

def p_expressions(parser):
    """expression : var ATTRIBUTION expression
                  | simple-expression
    """
    parser[0] = TreeNode(id='expression')

    [node, subtree] = parser[:2]

    node.insert_node(subtree)
    if len(parser) > 2:
        [_, exp] = parser[2:4]
        attrib_sym = TreeNode(raw=TOKENS_SYMBOLS.get('ATTRIBUTION'))
        attrib_node = TreeNode(id='ATTRIBUTION')
        attrib_node.insert_node(attrib_sym)
        node.insert_node(attrib_node)

        node.insert_node(exp)
        pass
    pass

def p_simple(parser):
    """simple-expression : additive-expression relop additive-expression
                         | additive-expression
    """
    parser[0] = TreeNode(id='simple-expression')

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
    parser[0] = TreeNode(id='additive-expression')

    [node, subtree] = parser[:2]

    node.insert_node(subtree)
    if len(parser) > 2:
        [addop, term] = parser[2:4]
        node.insert_node(addop)
        node.insert_node(term)
        pass
    pass

