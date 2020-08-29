# Model of a simple AND gate

def and_model(a: int, b: int) -> int:
    """ Model of AND gate """
    if(a == 1 and b == 1):
        return 1
    else:
        return 0
