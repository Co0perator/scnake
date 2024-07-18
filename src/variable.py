global var_dict
var_dict:dict = {
    "str": False,
    "int": False,
    "float": False,
    "complex": False,
    "list": False,
    "tuple": False,
    "range": False,
    "dict": False,
    "set": False,
    "frozenset": False,
    "bool": False,
    "bytes": False,
    "bytearray": False,
    "memoryview": False,
    "None": False, 
}

class Variable:
    types:dict = var_dict.copy()
    name:str = ""

    def __init__(self, name, types):
        self.name = name
        self.types = types

    def __init__(self, name):
        self.name = name
    
    def addType(self, type:str) -> None:
        if type in self.types.keys:
            self.types[type] = True
        else:
            raise TypeError