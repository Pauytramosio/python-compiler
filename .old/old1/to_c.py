import tokenizer
from itertools import groupby

def split_list_by_type(lst: list[object], delimiter_type: type) -> list[list[object]]:
    result:  list[object] = []
    sublist: list[object] = []
    for item in lst:
        if isinstance(item, delimiter_type):
            result.append(sublist)
            sublist = []
        else:
            sublist.append(item)
    result.append(sublist) 
    return result

def c(tokens: list[tokenizer.Token]) -> str:

    _c: str = ""
    
    def _incr(i: int) -> int: return i + 1
    def _decr(i: int) -> int: return i - 1
    incr: function = _incr
    decr: function = _decr

    imports:   list[str] = list();                                 build_imports: function = lambda: '\n'.join([f"#include <{module}>\n" for module in imports])
    main_func: str       = "int main(int argc, char* argv[]) {}"
    
    STATEMENTS: list[list[tokenizer.Token]] = split_list_by_type(tokens, tokenizer.EndStatement)
    i: int = 0
    j: int = 0
    statement: list[tokenizer.Token]
    token: tokenizer.Token
    while i < len(STATEMENTS):
        statement = STATEMENTS[i]
        while j < len(statement):
            token = statement[j]
            match type(token):
                case tokenizer.ExitKeyword:
                    main_func = main_func[:-1] + f"exit({statement[j + 1].value});" + "}"
                    imports.append("stdlib.h")
                    j += 2
        i += 1
    
    _c = build_imports() + main_func
    return _c