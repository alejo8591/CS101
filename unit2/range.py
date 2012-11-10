def set_range(a,b,c):
    if (a > b and a > c):
        if (b > c and b < a):
            return a - c
        else:
            return a - b
    elif (b > a and b > c):
        if (a > c and a < b):
            return b - c
        else:
            return b - a
    elif (c > a and c > b):
        if (a > b and a < c):
            return c - b
        else:
            return c - a
    elif (a == b and a > c):
        return a - c
    elif (b == c and b > a):
        return b - a
    elif (a == c and a > b):
        return a - b
    elif (a == b and b == c):
        return 0