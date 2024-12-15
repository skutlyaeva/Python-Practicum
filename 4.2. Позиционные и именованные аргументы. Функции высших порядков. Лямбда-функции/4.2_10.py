def secret_replace(t, **a):
    s = ''
    for i in t:
        if i in a:
            s += a[i][0]
            a[i] = a[i][1:] + (a[i][0],)
        else:
            s += i
    return s