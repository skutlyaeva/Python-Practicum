r = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1},
}
in_stock = {}


def order(*d):
    global in_stock
    for i in d:
        for j in r[i]:
            if r[i].get(j, 0) > in_stock[j]:
                break
        else:
            for j in r[i]:
                in_stock[j] -= r[i][j]
            return i

    if in_stock:
        return "К сожалению, не можем предложить Вам напиток"
