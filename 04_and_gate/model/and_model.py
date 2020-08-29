# Model of a simple AND gate

def and_model(a: int, b: int) -> int:
    """ model of AND gate """
    if(a == b):
        return 1
    elif(a != b):
        return 0
