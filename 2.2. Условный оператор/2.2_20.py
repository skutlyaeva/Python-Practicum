s1 = input()
s2 = input()
s3 = input()
m = []
if "зайка" in s1:
    m.append(s1)
if "зайка" in s2:
    m.append(s2)
if "зайка" in s3:
    m.append(s3)
print(min(m), len(min(m)))
