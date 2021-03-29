from lexer import TOKENS_SYMBOLS
from tree import TreeNode

def p_statement_list(parser):
    """statement-list : statement-list statement
                      | empty
    """
    parser[0] = TreeNode(id='STATEMENT_LIST')

    [node, subtree] = parser[:2]

    if len(parser) > 2:
        node.insert_nodes(subtree.nodes())
        [stmt] = parser[2:3]
        node.insert_node(stmt)
        pass
    pass

def p_statement(parser):
    """statement : expression-stmt
                 | compound-stmt
                 | selection-stmt
                 | iteration-stmt
                 | return-stmt
    """
    parser[0] = TreeNode(id='STATEMENT')

    [node, subtree] = parser

    node.insert_node(subtree)
    pass

def p_expression(parser):
    """expression-stmt : expression SEMICOLON
                       | SEMICOLON
    """
    parser[0] = TreeNode(id='EXPRESSION_STMT')

    [node, leaf] = parser[:2]


    if TOKENS_SYMBOLS.get('SEMICOLON') == leaf:
        leaf = TreeNode(id='SEMICOLON', raw=leaf)


    node.insert_node(leaf)

    if len(parser) > 2:
        node.insert_node(TreeNode(id='SEMICOLON', raw=TOKENS_SYMBOLS.get('SEMICOLON')))
        pass

    pass

def p_compound(parser):
    """compound-stmt : LBRACES local-declarations statement-list RBRACES"""
    parser[0] = TreeNode(id='COMPOUND_STMT')

    [node, _, local_decl, stmt_list, _] = parser

    node.insert_node(TreeNode(id='LBRACES', raw=TOKENS_SYMBOLS.get('LBRACES')))
    node.insert_node(local_decl)
    node.insert_node(stmt_list)
    node.insert_node(TreeNode(id='RBRACES', raw=TOKENS_SYMBOLS.get('RBRACES')))
    
    pass

def p_selection(parser):
    """selection-stmt : IF LPAREN expression RPAREN statement
                      | IF LPAREN expression RPAREN statement ELSE statement
    """
    parser[0] = TreeNode(id='SELECTION_STMT')

    [node, _, _, exp, _, stmt] = parser[:6]

    node.insert_node(TreeNode(id='IF', raw=TOKENS_SYMBOLS.get('IF')))
    node.insert_node(TreeNode(id='LPAREN', raw=TOKENS_SYMBOLS.get('LPAREN')))
    node.insert_node(exp)
    node.insert_node(TreeNode(id='RPAREN', raw=TOKENS_SYMBOLS.get('RPAREN')))
    node.insert_node(stmt)

    if len(parser) > 6:
        [_, stmt] = parser[6:8]
        node.insert_node(TreeNode(id='ELSE', raw=TOKENS_SYMBOLS.get('ELSE')))
        node.insert_node(stmt)
        pass

    pass

def p_iteration(parser):
    """iteration-stmt : WHILE LPAREN expression RPAREN statement"""
    parser[0] = TreeNode(id='ITERATION_STMT')

    [node, _, _, exp, _, stmt] = parser

    node.insert_node(TreeNode(id='WHILE', raw=TOKENS_SYMBOLS.get('WHILE')))
    node.insert_node(TreeNode(id='LPAREN', raw=TOKENS_SYMBOLS.get('LPAREN')))
    node.insert_node(exp)
    node.insert_node(TreeNode(id='RPAREN', raw=TOKENS_SYMBOLS.get('RPAREN')))
    node.insert_node(stmt)
    pass

def p_return(parser):
    """return-stmt : RETURN SEMICOLON
                   | RETURN expression SEMICOLON
    """
    parser[0] = TreeNode(id='RETURN_STMT')

    [node, _, leaf] = parser[:3]

    if TOKENS_SYMBOLS.get('SEMICOLON') == leaf:
        leaf = TreeNode(id='SEMICOLON', raw=leaf)

    node.insert_node(TreeNode(id='RETURN', raw=TOKENS_SYMBOLS.get('RETURN')))

    node.insert_node(leaf)

    if len(parser) > 3:
        leaf = TreeNode(id='SEMICOLON', raw=TOKENS_SYMBOLS.get('SEMICOLON'))

    pass
