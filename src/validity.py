import ast

def is_valid_python(code:str) -> bool :
    try:
        ast.parse(code)
    except SyntaxError:
        return False
    except TypeError:
        print("Type Error in input code")
        return False
    return True