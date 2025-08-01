from sys import argv
from grammar_scanner import Scanner
from grammar_parser import Parser
from grammar_interpreter import Interpreter

# Read in from the scanner
assert (len(argv) > 1), "Put the filename of the file you would like to parse as an argument."
s = Scanner(argv[1])
tokens = s.scan()
p = Parser(tokens)
database = p.parse()
i = Interpreter(database)
print(i.interpret())
# with open("output.py", "w") as out_file:
#     out_file.write(i.interpret())