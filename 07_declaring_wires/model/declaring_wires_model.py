# Model of a simple wire declaration

def declaring_wires_model(a: int, b: int, c: int, d: int):
    """ Model of simple wire declaration """

    z = int(OR(AND(a,b),AND(c,d)))
    z_n = NOT(z)
    return z, z_n;

def AND (a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def OR (a, b):
    if a == 1:
        return 1
    elif b == 1:
        return 1
    else:
        return 0

def NOT(a):
    if a == 1:
        return 0
    elif a == 0:
        return 1
