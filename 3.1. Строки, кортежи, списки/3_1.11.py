a = []
for i in range(n := int(input())):
    a.append(s := input())
s = (input()).lower()
for i in a:
    if s in i.lower():
        print(i)