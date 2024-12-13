def can_eat(h, c):
    x = abs(h[0] - c[0])
    y = abs(h[1] - c[1])
    return sorted([x, y]) == [1, 2]