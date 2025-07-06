from grammar_scanner import Token, TokenType 
from grammar_structure import Database

class Id:

    type : TokenType
    value : str

    def __init__(self, type : TokenType, value : str):
        self.type = type,
        self.value = value


class Production:
    
    name : str
    rhs : list[list[Id]]

    def __init__(self, name : str, rhs : list[list[Id]]):
        self.name = name
        self.rhs = rhs

    def __str__(self):
        out = self.name + " ::=\n  " + " |\n  ".join([" ".join([y.value for y in x]) for x in self.rhs]) + ".\n"
        return out


class Parser:

    tokens : list[Token] = []

    def advanceToken(self) -> Token:
        out : Token = self.tokens[0]
        self.tokens = self.tokens[1:]
        return out

    def match(self, t : TokenType) -> str:
        if self.expect(t):
            # print("match", self.tokens[0])
            out = self.tokens[0].token_value
            self.advanceToken()
            return out
        else:
            self.raiseError()

    def raiseError(self):
        raise Exception(self.tokens[0])
    
    def expect(self, t : TokenType) -> bool:
        return self.tokens[0].token_type == t
    
    def __init__(self, tokens : list):
        self.tokens = tokens
        
        
    def parse(self):

        match = self.match
        expect = self.expect
        raiseError = self.raiseError
        
        def file():
            productionList()
            match(TokenType.END)

        def productionList():
            if expect(TokenType.NON_TERMINAL):
                production()
                productionList()
            else:
                pass # lambda
        
        def production():
            
            name = match(TokenType.NON_TERMINAL)
            match(TokenType.PRODUCES)
            r : list[list[Id]] = []
            rhs(r)
            # print("Name:", name)
            p = Production(name, r)
            print(p)
            match(TokenType.PERIOD)

        def rhs(r : list[list[Id]]):
            rhsItem(r)
            rhsItemList(r)

        def rhsItem(r : list[list[Id]]):
            sl = []
            symbol(sl)
            symbolList(sl)
            r.append(sl)

        def symbol(sl : list[Id]):
            if expect(TokenType.NON_TERMINAL):
                sl.append(Id(TokenType.NON_TERMINAL, match(TokenType.NON_TERMINAL)))
            elif expect(TokenType.TERMINAL):
                sl.append(Id(TokenType.TERMINAL, match(TokenType.TERMINAL)))
            elif expect(TokenType.STRING):
                sl.append(Id(TokenType.STRING, match(TokenType.STRING)))
            elif expect(TokenType.LAMBDA):
                sl.append(Id(TokenType.LAMBDA, match(TokenType.LAMBDA)))
            else:
                raiseError()

        def symbolList(sl : list[Id]):
            if expect(TokenType.NON_TERMINAL) or expect(TokenType.TERMINAL) or expect(TokenType.STRING) or expect(TokenType.LAMBDA):
                symbol(sl)
                symbolList(sl)
            else:
                pass # lambda
        
        def rhsItemList(r : list[list[Id]]):
            if expect(TokenType.OR):
                match(TokenType.OR)
                rhsItem(r)
                rhsItemList(r)
            else:
                pass # lambda

        file()

