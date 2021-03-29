
import utils
from lexer import get_tokens
from parser import parser

if __name__ == '__main__':
    with open(utils.args.file) as file:
        as_str = file.read()
        if utils.args.lexer:
            for token in get_tokens(as_str):
                print(token.type, token.value)
                pass

        if utils.args.parser:

            graph = utils.Graph('asdasd', 'Parser')
            program = parser.parse(as_str)
            program.render(graph)

            graph.export()
            pass

        pass
    pass

