from __future__ import annotations

#%% Tokens

class Token:
    def __init__(self):
        self.value: object = None
    def __str__(self):
        return f"{type(self)} object at {id(self)}"
    def __repr__(self):
        return f"{type(self)};with;{self.value}"


class IntLiteral(Token):
    def __init__(self, value: int):
        super().__init__()
        self.value = value

class EndStatement(Token):
    def __init__(self):
        super().__init__()

class Keyword(Token):
    def __init__(self):
        super().__init__()

class ExitKeyword(Keyword):
    def __init__(self):
        super().__init__()


#%% Character detection methods - from the C standard library

def iswhitespace(char: str):
    return char in [' ', '\n']

def isalpha(char: str):
    return char.lower() in [
                            "a",
                            "b",
                            "c",
                            "d",
                            "e",
                            "f",
                            "g",
                            "h",
                            "i",
                            "j",
                            "k",
                            "l",
                            "m",
                            "n",
                            "o",
                            "p",
                            "q",
                            "r",
                            "s",
                            "t",
                            "u",
                            "v",
                            "w",
                            "x",
                            "y",
                            "z",
                            ]

def isdigit(char: str):
    return char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]

def isalnum(char: str):
    return isdigit(char) or isalpha(char)

#%% Tokenize (!)

def tokenize(code: str) -> list[Token]:
    tokens: list[Token] = list()
    i: int = 0
    while i < len(code):
        char: str = code[i]
        if isalpha(char):
            current: str = str()
            while isalnum(char):
                current += char
                i += 1
                char = code[i]
            match current:
                case "exit":
                    tokens.append(ExitKeyword())
                case _:
                    raise RuntimeError(f"Cannot comprehend name '{current}'")
        elif isdigit(char):
            current: str = str()
            while isdigit(char):
                char = code[i]
                if isdigit(char):
                    current += char
                    i += 1
                    char = code[i]
                else:
                    raise RuntimeError("Cannot comprehend integer literal " + current)
            tokens.append(IntLiteral(int(current)))
        elif char == ';':
            tokens.append(EndStatement())
            i += 1
        elif iswhitespace(char):
            i += 1
    return tokens