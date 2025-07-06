from grammar_parser import Production, Id

class Database:

    productions : list[Production] = []
    terminals : set[str] = []

    def __init__(self):
        pass