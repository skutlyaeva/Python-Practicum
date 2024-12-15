a = []
b = []
c = []


def enter_results(*numbers):
    global a, b, c
    a.extend(list(numbers))
    b = a[::2]
    c = a[1::2]


def get_sum():
    return round(sum(b), 2), round(sum(c), 2)


def get_average():
    return round(sum(b) / len(b), 2), round(sum(c) / len(c), 2)
