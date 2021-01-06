# Model of the 7458 chip

def 7458_model(p1a: int, p1b: int, p1c: int, p1d: int, p1e: int, p1f: int, p2a: int, p2b: int, p2c: int, p2d: int):
    """ Model of the 7458 chip """

    p1y = ((p1a AND p1b AND p1c) OR (p1f AND p1e AND p1d));
    p2y = ((p2a AND p2b) OR (p2c AND p2d));

    return p1y, p2y;

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
