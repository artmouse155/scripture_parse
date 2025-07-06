from grammar_parser import TokenType, Id, Production

class Interpreter:

    productions : list[Production]

    def __init__(self, productions : list[Production]):
        self.productions = productions

    def interpret(self) -> str:
        return "success!"