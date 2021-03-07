
import utils
from lexer import get_tokens

if __name__ == '__main__':
    with open(utils.args.file) as file:
        if utils.args.lexer:
            for token in get_tokens(file.read()):
                print(token.type, token.value)
                pass

        pass
    pass

