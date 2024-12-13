def merge(a, b):
    h = list(a)
    n = list(b)
    c = []
    while h and n:
        if h[0] > n[0]:
            c.append(n.pop(0))
        else:
            c.append(h.pop(0))
    c.extend(h)
    c.extend(n)
    return tuple(c)
