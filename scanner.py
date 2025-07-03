from enum import Enum

class TokenType(Enum):

    COMMA = "COMMA",
    DASH = "DASH",
    COLON = "COLON"
    SEMICOLON = "SEMICOLON"
    PERIOD = "PERIOD"
    AMPERSAND = "AMPERSAND"
    WORD = "WORD",
    NUMBER = "NUMBER",
    UNDEFINED = "UNDEFINED"
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
                case ",":
                    tokens.append(Token(TokenType.COMMA, t))
                case "-":
                    tokens.append(Token(TokenType.DASH, t))
                case "–":
                    tokens.append(Token(TokenType.DASH, t))
                case ":":
                    tokens.append(Token(TokenType.COLON, t))
                case ";":
                    tokens.append(Token(TokenType.SEMICOLON, t))
                case ".":
                    tokens.append(Token(TokenType.PERIOD, t))
                case "&":
                    tokens.append(Token(TokenType.AMPERSAND, t))
                case _:
                    # See if it is a word or number
                    if t.isalpha():
                        word = t
                        while (not self.isEOF() and self.peekNextToken().isalpha()):
                            t = self.advanceToken()
                            word += t
                            
                        tokens.append(Token(TokenType.WORD, word))
                    
                    elif(not self.isEOF() and self.peekNextToken().isnumeric()):
                        number = t
                        while self.peekNextToken().isnumeric():
                            t = self.advanceToken()
                            number += t

                        tokens.append(Token(TokenType.NUMBER, number))
                    else:
                        tokens.append(Token(TokenType.UNDEFINED, t))
        tokens.append(Token(TokenType.END, TokenType.END.value))
        return tokens
    