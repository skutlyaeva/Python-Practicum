import sys
a = []
for line in sys.stdin:
    for word in line.split():
        if word.lower() == word.lower()[::-1] and word not in a:
            a.append(word)
a.sort()
print(*a, sep="\n")