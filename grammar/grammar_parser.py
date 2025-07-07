from grammar_scanner import Token, TokenType

class Id:

    type : TokenType
    value : str

    def __init__(self, type : TokenType, value : str):
        self.type = type
        self.value = value

    def get_code_value(self) -> str:
        if (self.type == TokenType.NON_TERMINAL):
            return self.value[1:len(self.value)-1]
        return self.value


class Production:
    
    name : str
    rhs : list[list[Id]]
    first : list[list[Id]] # A list of non terminals which we expect to lead into the rhs.
    is_first_calculated : bool = False

    def __init__(self, name : str, rhs : list[list[Id]]):
        self.name = name
        self.rhs = rhs

    def calculate_first(self, get_first) -> list[list[Id]]:
        if not self.is_first_calculated:
            self.first : list[list[Id]] = []
            for item in self.rhs:
                item_first = []
                id = item[0]
                if ((id.type == TokenType.STRING) or (id.type == TokenType.TERMINAL)):
                    item_first.append(id)
                elif (id.type == TokenType.NON_TERMINAL):
                    item_first += [item for sublist in get_first(id.value) for item in sublist]
                self.first.append(item_first)
            self.is_first_calculated = True
        return self.first

    def __str__(self):
        out = self.name + " ::=\n  " + " |\n  ".join([" ".join([y.value for y in x]) for x in self.rhs]) + ".\n"
        out += "First: " + ("   \n".join(["(" + ", ".join([id.value for id in item]) + ")" for item in self.first]) if self.is_first_calculated else "NA") + '\n'
        return out
    
    def get_code_name(self) -> str:
        return self.name[1:len(self.name)-1]


class Database:

    productions : list[Production]
    terminals : set[str]

    def __init__(self, productions : list[Production], terminals : set[str]):
        self.productions = productions
        self.terminals = terminals

        def get_first(prod_name : str):
            production : Production = self.get_production(prod_name)
            return production.calculate_first(get_first)
        
        for production in self.productions:
            production.calculate_first(get_first)
        
    def get_production(self, name : str) -> Production:
        for production in self.productions:
            if production.name == name:
                return production
        raise Exception("Production not found:", name)
    
    def get_productions(self):
        return self.productions
    
    def __str__(self) -> str:
        out = ""
        for production in self.productions:
            out += str(production) + "\n"
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
        
        
    def parse(self) -> Database:

        match = self.match
        expect = self.expect
        raiseError = self.raiseError

        productions : list[Production] = []
        terminals : set[str] = set()
        
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
            productions.append(p)
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
                terminal_symbol = Id(TokenType.TERMINAL, match(TokenType.TERMINAL))
                sl.append(terminal_symbol)
                terminals.add(terminal_symbol.value)
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

        return Database(productions, terminals)

