import os
import math

w = os.path.dirname(__file__)
r = input()
k = os.path.getsize(w + "/" + r)
a = ["Б", "КБ", "МБ", "ГБ"]
index = 0
while k >= 1024 and index < len(a) - 1:
    k = math.ceil(k / 1024)
    index += 1
print(k, a[index], sep="")
