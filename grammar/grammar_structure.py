class Buffer:

    out : str = ""
    indent : int = 0

    def __init__(self):
        pass

    def write_line(self, s : str):
        self.out += "\t"*self.indent + s + "\n"

    def  increment_indent(self):
        self.indent += 1

    def  decrement_indent(self):
        self.indent -= 1

    def __str__(self):
        return self.out


class Statement:

    is_null : bool = False

    def __init__(self):
        pass

    def getlines(self, buffer : Buffer):
        buffer.write_line("")


class NullStmt(Statement):

    def __init__(self):
        self.is_null = True


class Sstr(Statement):

    value : str

    def __init__(self, value : str):
        self.value = value

    def getlines(self, buffer : Buffer):
        buffer.write_line(self.value)


class Import(Statement):

    f : str # "From"
    i : str # "Import"

    def __init__(self, f : str, i : str):
        self.f = f
        self.i = i

    def getlines(self, buffer : Buffer):
        out : str = ""
        if (self.f != ""):
            out += "from " + self.f + " "
        out += "import " + self.i
        buffer.write_line(out)


class Def(Statement):

    name : str
    arguments : list[str]
    statements : list[Statement]

    def __init__(self, name : str, arguments : list[str], statements : list[Statement]):
        self.name = name
        self.arguments = arguments
        self.statements = statements

    def getlines(self, buffer : Buffer):
        out : str = "def " + self.name + "(" + ", ".join(self.arguments) + "):"
        buffer.write_line(out)
        buffer.increment_indent()
        for statement in self.statements:
            statement.getlines(buffer)
        buffer.decrement_indent()
        buffer.write_line("")


class IfElifElse(Statement):
    
    conditions : list[str]
    body: list[list[Statement]]
    e: list[Statement]

    def __init__(self, conditions : list[str], body: list[list[Statement]], e: list[Statement]):
        self.conditions = conditions
        self.body = body
        self.e = e
    
    def getlines(self, buffer : Buffer):
        if (len(self.conditions) > 0):
            for i in range(len(self.conditions)):
                out = "if " if (i == 0) else "elif "
                out += self.conditions[i] + ":"
                buffer.write_line(out)
                buffer.increment_indent()
                for statement in self.body[i]:
                    statement.getlines(buffer)
                buffer.decrement_indent()
            if (len(self.e) > 0):
                buffer.write_line("else:")
                buffer.increment_indent()
                for statement in self.e:
                    statement.getlines(buffer)
                buffer.decrement_indent()
            

class Class(Statement):

    name : str
    statements : list[Statement]

    def __init__(self, name : str, statements : list[Statement]):
        self.name = name
        self.statements = statements

    def getlines(self, buffer : Buffer):
        out : str = "class " + self.name + ":"
        buffer.write_line(out)
        buffer.increment_indent()
        buffer.write_line("")
        for statement in self.statements:
            statement.getlines(buffer)
        buffer.decrement_indent()
        buffer.write_line("")


class FileStructure:

    statements : list[Statement]

    def __init__(self, statements : list[Statement]):
        self.statements = statements

    def __str__(self):
        buffer : Buffer = Buffer()

        for statement in self.statements:
            statement.getlines(buffer)

        return str(buffer)