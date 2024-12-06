input_filename = input()
a = []
with open(input_filename, "r", encoding="UTF-8") as input_file:
    for line in input_file:
        a += map(int, line.split())

k = len(a)
pk = len([x for x in a if x > 0])
minn = min(a)
maxx = max(a)
summ = sum(a)
c = round(summ / k, 2)
print(
    k,
    pk,
    minn,
    maxx,
    summ,
    c,
    sep="\n",
)
