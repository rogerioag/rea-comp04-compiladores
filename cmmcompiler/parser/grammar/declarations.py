from lexer import TOKENS_SYMBOLS
from tree import TreeNode

def p_declaration_list(parser):
    """declaration-list : declaration-list declaration
                        | declaration
    """
    parser[0] = TreeNode(id='declaration-list')

    [node, subtree] = parser[:2]

    if len(parser) > 2:
        node.insert_nodes(subtree.nodes())
        [dec] = parser[2:3]
        node.insert_node(dec)
        pass
    else:
        node.insert_node(subtree)
    pass

def p_declaration(parser):
    """declaration : var-declaration
                   | fun-declaration
    """
    parser[0] = TreeNode(id='declaration')

    [node, subtree] = parser

    node.insert_node(subtree)
    pass

def p_var_declaration(parser):
    """var-declaration : type-specifier id SEMICOLON
                       | type-specifier id LBRACKETS number RBRACKETS SEMICOLON
    """
    parser[0] = TreeNode(id='var-declaration')

    [node, type_spec, id_node, symbol] = parser[:4]

    node.insert_node(type_spec)
    node.insert_node(id_node)


    if TOKENS_SYMBOLS.get('SEMICOLON') == symbol:
        ## node.insert_node(TreeNode(id='SEMICOLON', raw=TOKENS_SYMBOLS.get('SEMICOLON')))
        #sym = TreeNode(raw=TOKENS_SYMBOLS.get('SEMICOLON'))
        #sym_node = TreeNode(id='SEMICOLON')
        #sym_node.insert_node(sym)
        #node.insert_node(sym_node)
        node.insert_node_with_child(TreeNode(id='SEMICOLON'), TreeNode(raw=TOKENS_SYMBOLS.get('SEMICOLON')))
        pass
    elif TOKENS_SYMBOLS.get('LBRACKETS') == symbol:
        ##node.insert_node(TreeNode(id='LBRACKETS', raw=TOKENS_SYMBOLS.get('LBRACKETS')))
        #sym = TreeNode(raw=TOKENS_SYMBOLS.get('LBRACKETS'))
        #sym_node = TreeNode(id='LBRACKETS')
        #sym_node.insert_node(sym)
        #node.insert_node(sym_node)
        node.insert_node_with_child(TreeNode(id='LBRACKETS'), TreeNode(raw=TOKENS_SYMBOLS.get('LBRACKETS')))

        [number] = parser[4:5]
        node.insert_node(number)

        ##node.insert_node(TreeNode(id='RBRACKETS', raw=TOKENS_SYMBOLS.get('RBRACKETS')))
        #sym = TreeNode(raw=TOKENS_SYMBOLS.get('RBRACKETS'))
        #sym_node = TreeNode(id='RBRACKETS')
        #sym_node.insert_node(sym)
        #node.insert_node(sym_node)
        node.insert_node_with_child(TreeNode(id='RBRACKETS'), TreeNode(raw=TOKENS_SYMBOLS.get('RBRACKETS')))

        ##node.insert_node(TreeNode(id='SEMICOLON', raw=TOKENS_SYMBOLS.get('SEMICOLON')))
        #sym = TreeNode(raw=TOKENS_SYMBOLS.get('SEMICOLON'))
        #sym_node = TreeNode(id='SEMICOLON')
        #sym_node.insert_node(sym)
        #node.insert_node(sym_node)
        node.insert_node_with_child(TreeNode(id='SEMICOLON'), TreeNode(raw=TOKENS_SYMBOLS.get('SEMICOLON')))


        pass

    pass

def p_fun_declaration(parser):
    """fun-declaration : type-specifier id LPAREN params RPAREN compound-stmt"""
    parser[0] = TreeNode(id='fun-declaration')

    [node, type_spec, id_node, _, params, _, compound] = parser

    node.insert_node(type_spec)
    node.insert_node(id_node)
    # node.insert_node(TreeNode(id='LPAREN', raw=TOKENS_SYMBOLS.get('LPAREN')))
    node.insert_node_with_child(TreeNode(id='LPAREN'), TreeNode(raw=TOKENS_SYMBOLS.get('LPAREN')))
    node.insert_node(params)
    # node.insert_node(TreeNode(id='RPAREN', raw=TOKENS_SYMBOLS.get('RPAREN')))
    node.insert_node_with_child(TreeNode(id='RPAREN'), TreeNode(raw=TOKENS_SYMBOLS.get('RPAREN')))
    node.insert_node(compound)

    pass

def p_local_declarations(parser):
    """local-declarations : local-declarations var-declaration
                          | empty
    """
    parser[0] = TreeNode(id='local-declarations')

    [node, subtree] = parser[:2]

    node.insert_node(subtree)

    if len(parser) > 2:
        [var] = parser[2:3]
        node.insert_node(var)
        pass
    pass
