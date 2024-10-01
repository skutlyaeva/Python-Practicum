a = int(input())
b = [a // 100, a // 10 % 10, a % 10]
s = max(b) + min(b)
o = 2 * (sum(b) - s)
if o == s:
    print("YES")
else:
    print("NO")