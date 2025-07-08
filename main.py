from sys import argv, setrecursionlimit
from scanner import Scanner
from parser import Parser

setrecursionlimit(10000)

# Read in from the scanner
assert (len(argv) > 1), "Put the filename of the file you would like to parse as an argument."
s = Scanner(argv[1])
tokens = s.scan()
# for token in tokens:
#     print(token)
p = Parser(tokens)
p.parse()