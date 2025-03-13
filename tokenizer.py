import chars

#%% TOKENS
class Token:
    def __init__(self, value: object = None):
        self.value: object = None
    def __repr__(self):
        return f"{type(self)}-value:{self.value}@{id(self)}"
    def __str__(self):
        return f"{type(self)} object ({self.value}) at {id(self)}"

class Break(Token):
    def __init__(self):
        super().__init__()

class Keyword(Token):
    def __init__(self):
        super().__init__()

class ExitKeyword(Keyword):
    def __init__(self):
        super().__init__()


class Literal(Token):
    def __init__(self, value):
        super().__init__()
        self.value = value

class IntLiteral(Literal):
    def __init__(self, value):
        super().__init__(value)

#%%

def tokenize(scope: str) -> list:
    tokens:    list[list[Token]] = list()
    statement: list[Token]       = list()

    ichar: int = 0
    while ichar < len(scope):
        if chars.isalpha(scope[ichar]):
            current: str = str()
            while chars.isalnum(scope[ichar]):
                current += scope[ichar]
                ichar += 1
            if current == "exit":
                statement.append(ExitKeyword())
            else:
                raise RuntimeError(f"Cannot recognize symbol {current}")
        elif chars.isdigit(scope[ichar]):
            current: str = str()
            while chars.isdigit(scope[ichar]):
                current += scope[ichar]
                ichar += 1
            statement.append(IntLiteral(current))
        elif chars.isspace(scope[ichar]):
            ichar += 1
        elif scope[ichar] == ';':
            tokens.append(statement)
            statement = list()
            if ichar + 1 == len(scope):
                break
            else:
                ichar += 1
        else:
            raise RuntimeError(f"Unrecognized character: {scope[ichar]}")


    return tokens
