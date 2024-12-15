def to_string(*a, sep=' ', end='\n'):
    s = ''
    a = list(a)
    while a:
        i = a.pop(0)
        s += str(i)
        if a:
            s += sep
    return s + end