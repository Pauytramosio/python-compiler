from typing import Callable
import tokenizer

def translate(tokens: list[list[tokenizer.Token]]) -> str:

    mainf:  str        =  "int main(int argc, char* argv[]) {"
    include: list[str] =                                list(); build: Callable[[], str] = (lambda: "\n".join([f"#include <{toinclude}>" for toinclude in include]))

    i: int = 0
    j: int = 0
    while i < len(tokens):
        while j < len(tokens[i]):
            match type(tokens[i][j]):
                case tokenizer.ExitKeyword:
                    include.append("stdlib.h")
                    mainf += f"exit({tokens[i][j+1].value})"
                    j += 1
                case tokenizer.IntLiteral:
                    mainf += tokens[i][j].value
            j += 1
        mainf += ';'
        i += 1
    
    return build() + '\n' + mainf + '}'