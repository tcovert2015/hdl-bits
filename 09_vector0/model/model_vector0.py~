# Model of the 7458 chip

def model_7458(p1a: int, p1b: int, p1c: int, p1d: int, p1e: int, p1f: int, p2a: int, p2b: int, p2c: int, p2d: int):
    """ Model of the 7458 chip """

    p1y = OR  ((AND(p1a, AND(p1c, p1b))),  (AND(p1f, AND(p1e, p1d)))   );
    p2y = OR  ((AND(p2a, p2b)),            (AND(p2c, p2d))   );

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
