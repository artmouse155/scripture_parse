from sys import argv
from grammar_scanner import Scanner

# Read in from the scanner
assert (len(argv) > 1), "Put the filename of the file you would like to parse as an argument."
s = Scanner(argv[1])
tokens = s.scan()
for token in tokens:
    print(token)