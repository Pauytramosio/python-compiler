import chars

#%% TOKENS
class Token:
    def __init__(self):
        value: object
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
    