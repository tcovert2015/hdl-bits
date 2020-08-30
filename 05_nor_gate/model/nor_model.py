# Model of a simple NOR gate

def nor_model(a: int, b: int) -> int:
    """ Model of NOR gate """
    if(a == 1 or b == 1):
        return 0
    else:
        return 1
