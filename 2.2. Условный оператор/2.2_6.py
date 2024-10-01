g = int(input())
a = [1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600]
if g % 4 == 0 and g not in a:
    print("YES")
else:
    print("NO")