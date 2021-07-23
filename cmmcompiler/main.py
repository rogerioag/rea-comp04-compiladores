
import utils
from lexer import get_tokens
from parser import parser
from semantic import sema, Semantic
from gencode import gencode, GenCode
from tree import TreeNode

import logging
logging.basicConfig(
    filename = "cmmcompiler.log",
    encoding='utf-8',
    level = logging.DEBUG,
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s")
log = logging.getLogger()

syntax_tree = None
reduced_syntax_tree = None

def execute_lexical_analysis(source_input):
    log.info("[lexer]: Executing Lexical Analysis.")
    for token in get_tokens(source_input):
        print(token.type, token.value)
    return

def execute_syntax_analisys(source_input):
    log.info("[parser]: Executing Syntax Analysis.")
    syntax_tree = parser.parse(source_input)
    if syntax_tree != ():
        print("Generating Syntax Tree Graph...")
        graph = utils.Graph(utils.args.file, 'Sintax Tree')
        # program = parser.parse(source_input)
        syntax_tree.render(graph)
        graph.export()
    return syntax_tree

def execute_semantic_analisys(syntax_tree):
    log.info("[sema]: Executing Semantic Analysis.")
    sema = Semantic(syntax_tree)
    sema.check_semantic_rules()
    return reduced_syntax_tree

def execute_code_generation(reduced_syntax_tree):
    log.info("[gencode]: Executing Code Generation.")
    gencode = GenCode(reduced_syntax_tree)
    gencode.generate()
    return

if __name__ == '__main__':
    with open(utils.args.file) as file:
        source_input = file.read()
        if utils.args.lexer:
            execute_lexical_analysis(source_input)    
        pass

        if utils.args.parser:
            syntax_tree = execute_syntax_analisys(source_input) 
        pass
        
        if utils.args.semantic:
            if syntax_tree != ():
                reduced_syntax_tree = execute_semantic_analisys(syntax_tree)
            else:
                syntax_tree = execute_syntax_analisys(source_input)
                reduced_syntax_tree = execute_semantic_analisys(syntax_tree)
            pass
        pass

        if utils.args.gencode:
            if reduced_syntax_tree != None:
                execute_code_generation(reduced_syntax_tree)
            else:
                syntax_tree = execute_syntax_analisys(source_input)
                if syntax_tree != ():
                    reduced_syntax_tree = execute_semantic_analisys(syntax_tree)
                    execute_code_generation(reduced_syntax_tree)
                pass

        pass
        
    pass
