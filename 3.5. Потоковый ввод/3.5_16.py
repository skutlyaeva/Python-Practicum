import sys
t = input().lower()
ok = False
a = [line.strip() for line in sys.stdin]
for i in a:
    with open(i, "r", encoding="UTF-8") as file:
        c = file.read()
        c = ' '.join(c.lower().split())
        if t in c:
            ok = True
            print(i)
if ok is False:
    print("404. Not Found")