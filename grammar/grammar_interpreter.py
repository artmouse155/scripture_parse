from grammar_parser import TokenType, Id, Production, Database
from grammar_structure import *

class Interpreter:

    database : Database
    fileStructure : FileStructure

    def __init__(self, database : Database):
        self.database = database

    def interpret(self) -> str:

        endl : Statement = NullStmt()

        lines : list[Statement] = []
        lines.append(Import("enum", "Enum"))
        lines.append(endl)

        
        enum_lines : list[Statement] = []
        for terminal in self.database.terminals:
            enum_lines.append(Sstr(terminal + " = \"" + terminal + "\""))
        if (len(self.database.terminals) == 0):
            enum_lines.append(Sstr("pass # No terminals found"))
        lines.append(Class("TokenType(Enum)", enum_lines))

        p_class_lines : list[Statement] = []
        p_class_lines.append(Sstr("# Implement class variables here..."))
        p_class_lines.append(endl)
        p_class_lines.append(Def("__init__", ["self"], [Sstr("pass # Implement")]))
        p_class_lines.append(Def("match", ["self", "t : TokenType | str"], [Sstr("pass # Implement")]))
        p_class_lines.append(Def("expect", ["self", "t : TokenType | str"], [Sstr("pass # Implement")]))
        p_class_lines.append(Def("raiseError", ["self"], [Sstr("pass # Implement")]))

        p_class_function_lines : list[Statement] = []
        p_class_function_lines.append(endl)
        p_class_function_lines.append(Sstr("match = self.match"))
        p_class_function_lines.append(Sstr("expect = self.expect"))
        p_class_function_lines.append(Sstr("raiseError = self.raiseError"))
        p_class_function_lines.append(endl)
        for production in self.database.get_productions():
            else_stmt : Statement = Sstr("raiseError()")
            conditions = []
            body = []
            for i in range(len(production.rhs)):
                tokens : list[Id] = production.rhs[i]
                first : list[Id] = production.first[i]
                if (len(first) == 0 and len(tokens) == 1 and tokens[0].type == TokenType.LAMBDA):
                    else_stmt : Statement = Sstr("pass # lambda")
                else:
                    conditions.append(" or ".join(["expect(" + ("TokenType." if (x.type == TokenType.TERMINAL) else "") + x.value + ")" for x in first]))
                    inner_body : list[Statement] = []
                    for token in tokens:
                        
                        if (token.type == TokenType.NON_TERMINAL):
                            inner_body.append(Sstr(token.get_code_value() + "()"))
                        elif (token.type == TokenType.TERMINAL):
                            inner_body.append(Sstr("match(TokenType." + token.get_code_value() + ")"))
                        elif (token.type == TokenType.STRING):
                            inner_body.append(Sstr("match(" + token.get_code_value() + ")"))
                    body.append(inner_body)
            f : Def = Def(production.get_code_name(), [], [IfElifElse(conditions, body, [else_stmt])])
            p_class_function_lines.append(f)
        if len(self.database.get_productions()) > 0:
            p_class_function_lines.append(Sstr(self.database.get_productions()[0].get_code_name() + "()"))
        p_class_lines.append(Def("parse", ["self"], p_class_function_lines))
        lines.append(Class("Parser", p_class_lines))
        self.fileStructure = FileStructure(lines)
        return str(self.fileStructure)