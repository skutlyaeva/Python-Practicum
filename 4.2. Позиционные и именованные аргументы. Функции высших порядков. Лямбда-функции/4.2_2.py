def make_matrix(s, c=0):
    if isinstance(s, int):
        s = [s, s]
    result = [[c] * s[0] for i in range(s[1])]
    return result
