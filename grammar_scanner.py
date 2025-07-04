from enum import Enum

class TokenType(Enum):

    STRING = "STRING"
    NON_TERMINAL = "NON_TERMINAL"
    TERMINAL = "TERMINAL"
    COMMENT = "COMMENT"
    PRODUCES = "::="
    PERIOD = "."
    OR = "|"
    LAMBDA = "lambda"
    UNDEFINED = "?"
    END = "END"

class Token:

    token_type : TokenType = TokenType.UNDEFINED
    token_value : str = ""

    def __init__(self, token_type : TokenType, token_value : str):
        self.token_type = token_type
        self.token_value = token_value

    def __str__(self):
        return "(" + self.token_type.name + ", \"" + self.token_value + "\")"

class Scanner:

    content : str = ""

    def advanceToken(self) -> str:
        out : str = self.content[0]
        self.content = self.content[1:]
        return out
    
    def expectTokens(self, type : TokenType, t : str, tokens : str) -> Token:
        out = t
        for i in range(len(tokens)):
            if (not self.isEOF() and self.peekNextToken() == tokens[i]):
                t = self.advanceToken()
                out += t
            else:
                return Token(TokenType.UNDEFINED, out)
        return Token(type, out)
    
    def peekNextToken(self) -> str:
        return self.content[0]
    
    def isEOF(self) -> bool:
        return (self.content == "")

    def __init__(self, filename):
        with open(filename, "r", encoding="utf8") as f:
            self.content = f.read()

    def scan(self):
        tokens = []
        while (not self.isEOF()):
            t : str = self.advanceToken()
            # Get rid of whitespace!
            while (not self.isEOF() and t.isspace()):
                t = self.advanceToken()

            if (t.isspace()):
                break

            match t:
                case ".":
                    tokens.append(Token(TokenType.PERIOD, t))
                case "|":
                    tokens.append(Token(TokenType.OR, t))
                case ":":
                    tokens.append(self.expectTokens(TokenType.PRODUCES, t, ":="))
                case "l":
                    tokens.append(self.expectTokens(TokenType.LAMBDA, t, "ambda"))
                case "#":
                    word = t

                    while (not self.isEOF()) and (self.peekNextToken() != "\n"):
                        t = self.advanceToken()
                        word += t
                    if (self.isEOF()):
                        tokens.append(Token(TokenType.UNDEFINED, word))
                    else:
                        t = self.advanceToken()
                        word += t
                        tokens.append(Token(TokenType.COMMENT, word))
                case "<":
                    word = t

                    while (not self.isEOF()) and (self.peekNextToken() != ">"):
                        t = self.advanceToken()
                        word += t
                    if (self.isEOF()):
                        tokens.append(Token(TokenType.UNDEFINED, word))
                    else:
                        t = self.advanceToken()
                        word += t
                        tokens.append(Token(TokenType.NON_TERMINAL, word))
                case "\"":
                    word = t

                    while (not self.isEOF()) and (self.peekNextToken() != "\""):
                        t = self.advanceToken()
                        word += t
                    if (self.isEOF()):
                        tokens.append(Token(TokenType.UNDEFINED, word))
                    else:
                        t = self.advanceToken()
                        word += t
                        tokens.append(Token(TokenType.STRING, word))
                    
                case _:
                    # See if it is a word or number
                    if t.isalpha() and t.isupper():
                        word = t
                        while (not self.isEOF() and ((self.peekNextToken().isalpha() and self.peekNextToken().isupper()) or self.peekNextToken().isnumeric())):
                            t = self.advanceToken()
                            word += t
                            
                        tokens.append(Token(TokenType.TERMINAL, word))
                    else:
                        tokens.append(Token(TokenType.UNDEFINED, t))
        tokens.append(Token(TokenType.END, TokenType.END.value))
        return tokens
    