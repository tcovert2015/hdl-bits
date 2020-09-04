# Model of a simple XNOR gate

def xnor_model(a: int, b: int) -> int:
    """ Model of XNOR gate """
    if(a == b):
        return 1
    else:
        return 0
