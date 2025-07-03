from enum import Enum

class TokenType(Enum):
    BOOK = "BOOK",
    NUMBER = "NUMBER",
    COMMA = "COMMA",
    DASH = "DASH",
    COLON = "COLON"
    SEMICOLON = "SEMICOLON"
    VERSE = "VERSE",
    UNDEFINDED = "UNDEFINED"
    END = "END"

class Token:

    token_type = TokenType.UNDEFINED

    def __init__(self):
        pass

class Scanner:

    content = ""

    def __init__(self, filename):
        with open(filename, "r", encoding="utf8") as f:
            self.content = f.read()

    def scan(self):
        while (len(self.content) > 0):
            pass

    