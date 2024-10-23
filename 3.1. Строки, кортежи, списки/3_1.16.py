L = int(input())
lines = []
for i in range(int(input())):
    lines.append(input())
for i in lines:
    if L > 3:
        if len(i) >= L - 3:
            i = i[:L - 3] + "..."
        else:
            if L == 4:
                i = i + "..."
        print(i)
        L -= len(i)