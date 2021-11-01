from lexer import TOKENS_SYMBOLS
from tree import TreeNode

import logging
log = logging.getLogger()

def p_params(parser):
    """params : param-list
              | void
    """
    parser[0] = TreeNode(id='params')

    [node, subtree] = parser
    node.insert_node(subtree)
    pass

def p_params_error(parser):
    """params : error
    """
    print("Erro: 'param-list' ou 'void' esperado.")
    parser[0] = TreeNode(id='ERROR::{}'.format(parser.lineno(1)))

    [node, subtree] = parser
    node.insert_node(subtree)
    
    log.error("Syntax error parsing 'params' rule at line {}".format(parser.lineno(1)))
        
    pass

def p_param_list(parser):
    """param-list : param-list COMMA param
                  | param
    """
    parser[0] = TreeNode(id='param-list')

    [node, subtree] = parser[:2]

    if len(parser) > 2:
        node.insert_nodes(subtree.nodes())

        [_, param] = parser[2:4]
        # node.insert_node(TreeNode(id='COMMA', raw=TOKENS_SYMBOLS.get('COMMA')))
        node.insert_node_with_child(TreeNode(id='COMMA'), TreeNode(raw=TOKENS_SYMBOLS.get('COMMA')))
        node.insert_node(param)
    else:
        node.insert_node(subtree)


    pass

def p_param(parser):
    """param : type-specifier id
             | type-specifier id LBRACKETS RBRACKETS
    """
    parser[0] = TreeNode(id='param')

    [node, subtree, id_node] = parser[:3]
    node.insert_node(subtree)
    node.insert_node(id_node)

    if len(parser) > 3:
        # node.insert_node(TreeNode(id='LBRACKETS', raw=TOKENS_SYMBOLS.get('LBRACKETS')))
        node.insert_node_with_child(TreeNode(id='LBRACKETS'), TreeNode(raw=TOKENS_SYMBOLS.get('LBRACKETS')))
        # node.insert_node(TreeNode(id='RBRACKETS', raw=TOKENS_SYMBOLS.get('RBRACKETS')))
        node.insert_node_with_child(TreeNode(id='RBRACKETS'), TreeNode(raw=TOKENS_SYMBOLS.get('RBRACKETS')))
        pass

    pass
