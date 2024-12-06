import json
import sys
a = [line.strip() for line in sys.stdin]
with open("scoring.json", "r", encoding="UTF-8") as input_file:
    data = json.load(input_file)
p = []
for i in data:
    t = i["points"] // len(i["tests"])
    for test in i["tests"]:
        p.append((test["pattern"], t))
if len(a) != len(p):
    print("Неверное количество выходных строк")
else:
    r = 0
    for i in range(len(p)):
        answer = a[i]
        pattern = p[i][0]
        points = p[i][1]
        if answer == pattern:
            r += points
    print(r)
