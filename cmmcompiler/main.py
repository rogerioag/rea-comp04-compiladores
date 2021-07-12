
import utils
from lexer import get_tokens
from parser import parser
from tree import TreeNode

if __name__ == '__main__':
    with open(utils.args.file) as file:
        source_input = file.read()
        if utils.args.lexer:
            for token in get_tokens(source_input):
                print(token.type, token.value)
                pass

        if utils.args.parser:

            syntax_tree = parser.parse(source_input)

            if syntax_tree != ():
                print("Generating Syntax Tree Graph...")
                graph = utils.Graph(utils.args.file, 'Sintax Tree')
                # program = parser.parse(source_input)
                syntax_tree.render(graph)
                graph.export()
            pass

        pass
    pass
