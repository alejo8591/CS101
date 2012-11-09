def set_range(a,b,c):
    if a > b:
        if b > c:
            return a - c
        else:
            return a - b
    elif b > a:
        if a > c:
            return b - c
        else:
            return b - a
    elif c > a:
        if a > b:
            return c - b
        else:
            return c - a
    elif a == b:
        if a > c:
            return a - c
            