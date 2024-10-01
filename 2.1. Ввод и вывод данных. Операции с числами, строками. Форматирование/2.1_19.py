a = input()
b = int(input())
c = int(input())
d = int(input())
k = f"{a}"
k1 = k.rjust(28, " ")
k2 = f"{c}кг * {b}руб/кг"
k3 = k2.rjust(29, " ")
s = f"{c * b}руб"
s1 = s.rjust(28, " ")
h = f"{d}руб"
h1 = h.rjust(26, " ")
g = f"{d - (c * b)}руб"
g1 = g.rjust(28, " ")
print("================Чек================")
print("Товар:", k1)
print("Цена:", k3)
print("Итого:", s1)
print("Внесено:", h1)
print("Сдача:", g1)
print("===================================")