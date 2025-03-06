import tokenizer
from itertools import groupby

def split_list_by_type(lst, delimiter_type):
    result = []
    sublist = []
    for item in lst:
        if isinstance(item, delimiter_type):
            result.append(sublist)
            sublist = []
        else:sublist.append(item)
    result.append(sublist) 
    return result

def assemble(tokens: list[tokenizer.Token]) -> str:
    asm = "global _start\n_start:\n"
    for i, statement in enumerate(split_list_by_type(tokens, tokenizer.EndStatement)):
        for j, token in enumerate(statement):
            if type(token) == tokenizer.ExitKeyword:
                asm += f"        mov rax, 60\n        mov rdi, {statement[j+1].value}\n        syscall"
    return asm