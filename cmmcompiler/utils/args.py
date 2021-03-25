__all__ = ['args']
import argparse

parser = argparse.ArgumentParser(description='A C- Compiler', prog='python3 main.py')

parser.add_argument('-l', '--lexer', action='store_true',
                    help='Execute only the lexical analysis at source code and outputs a list of tokens')

parser.add_argument('file', help='Source Code in C-')

args = parser.parse_args()
args.complete = not (args.lexer)
