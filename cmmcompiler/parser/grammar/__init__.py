import re as regex

from lexer import TOKENS_SYMBOLS
from tree import TreeNode

from .declarations import *
from .expressions import *
from .operations import *
from .params import *
from .types import *
from .statements import *

def p_program(parser):
    """program : declaration-list"""
    parser[0] = TreeNode(id='PROGRAM')

    [node, declaration_list] = parser

    node.insert_node(declaration_list)
    pass

def p_var(parser):
    """var : id
           | id LBRACKETS expression RBRACKETS
    """
    parser[0] = TreeNode(id='VAR')

    [node, id_node] = parser[:2]

    node.insert_node(id_node)

    if len(parser) > 2:
        [_, expression] = parser[2:4]
        node.insert_node(TreeNode(id='LBRACKETS', raw=TOKENS_SYMBOLS.get('LBRACKETS')))
        node.insert_node(expression)
        node.insert_node(TreeNode(id='RBRACKETS', raw=TOKENS_SYMBOLS.get('RBRACKETS')))
        pass
    pass


# TODO: Estava faltando term. Verificar a montagem do nó.

def p_term(parser):
    """term : term mulop factor
            | factor
    """
    parser[0] = TreeNode(id='TERM')

    [node, leaf] = parser[:2]
    node.insert_node(leaf)

    if len(parser) > 2:
        [mulop] = parser[2:3]
        node.insert_node(mulop)
        [factor] = parser[3:4]
        node.insert_node(factor)
        pass
    pass

def p_factor(parser):
    """factor : LPAREN expression RPAREN
              | var
              | call
              | number
    """
    parser[0] = TreeNode(id='FACTOR')

    [node, leaf] = parser[:2]

    if TOKENS_SYMBOLS.get('LPAREN') == leaf:
        [exp] = parser[2:3]

        node.insert_node(TreeNode(id='LPAREN', raw=TOKENS_SYMBOLS.get('LPAREN')))
        node.insert_node(exp)
        node.insert_node(TreeNode(id='RPAREN', raw=TOKENS_SYMBOLS.get('RPAREN')))
    else:
        node.insert_node(leaf)
        pass

    pass

def p_call(parser):
    """call : id LPAREN args RPAREN"""
    parser[0] = TreeNode(id='CALL')

    [node, id_raw, _, args, _] = parser

    id_node = TreeNode(id='ID')
    id_node.insert_node(TreeNode(raw=id_raw))

    node.insert_node(id_node)
    node.insert_node(TreeNode(id='LPAREN', raw=TOKENS_SYMBOLS.get('LPAREN')))
    node.insert_node(args)
    node.insert_node(TreeNode(id='RPAREN', raw=TOKENS_SYMBOLS.get('RPAREN')))
    pass

def p_id(parser):
    """id : ID"""
    parser[0] = TreeNode(id='ID')
    [node, id_raw] = parser

    node.insert_node(TreeNode(raw=id_raw))
    pass

def p_number(parser):
    """number : NUMBER"""
    parser[0] = TreeNode(id='NUMBER')
    [node, number] = parser

    node.insert_node(TreeNode(raw=number))
    pass

def p_args(parser):
    """args : arg-list
            | empty
    """
    parser[0] = TreeNode(id='ARGS')
    [node, leaf] = parser

    node.insert_node(leaf)
    pass

def p_arg_list(parser):
    """arg-list : arg-list COMMA expression
                | expression
    """
    parser[0] = TreeNode(id='ARG_LIST')
    [node, leaf] = parser[:2]

    node.insert_node(leaf)
    if len(parser) > 2:
        [_, exp] = parser[2:4]
        node.insert_node(TreeNode(id='COMMA', raw=TOKENS_SYMBOLS.get('COMMA')))
        node.insert_node(exp)
        pass
    pass

def p_empty(parser):
    """empty :"""
    parser[0] = TreeNode(id='EMPTY')
    pass

def p_error(parser):

    print(parser)
    pass