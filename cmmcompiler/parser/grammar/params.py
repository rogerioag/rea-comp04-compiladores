from lexer import TOKENS_SYMBOLS
from tree import TreeNode

def p_params(parser):
    """params : param-list
              | void
    """
    parser[0] = TreeNode(id='PARAMS')

    [node, subtree] = parser
    node.insert_node(subtree)
    pass

def p_param_list(parser):
    """param-list : param-list COMMA param
                  | param
    """
    parser[0] = TreeNode(id='PARAM_LIST')

    [node, subtree] = parser[:2]

    if len(parser) > 2:
        node.insert_nodes(subtree.nodes())

        [_, param] = parser[2:4]
        node.insert_node(TreeNode(id='COMMA', raw=TOKENS_SYMBOLS.get('COMMA')))
        node.insert_node(param)
    else:
        node.insert_node(subtree)


    pass

def p_param(parser):
    """param : type-specifier id
             | type-specifier id LBRACKETS RBRACKETS
    """
    parser[0] = TreeNode(id='PARAM')

    [node, subtree, id_node] = parser[:3]
    node.insert_node(subtree)
    node.insert_node(id_node)

    if len(parser) > 3:
        node.insert_node(TreeNode(id='LBRACKETS', raw=TOKENS_SYMBOLS.get('LBRACKETS')))
        node.insert_node(TreeNode(id='RBRACKETS', raw=TOKENS_SYMBOLS.get('RBRACKETS')))
        pass

    pass
