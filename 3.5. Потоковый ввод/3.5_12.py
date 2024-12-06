import sys
input_filename = input()
even_filename = input()
odd_filename = input()
equal_filename = input()
with open(input_filename, "r", encoding="UTF-8") as input_file:
    for line in input_file:
        a, b, c = [], [], []
        for s in line.split():
            ac = sum([s.count(str(x)) for x in range(0, 9, 2)])
            bc = sum([s.count(str(x)) for x in range(1, 10, 2)])
            if ac > bc:
                a.append(s)
            elif ac < bc:
                b.append(s)
            else:
                c.append(s)

        for filename, list in zip(
                [even_filename, odd_filename, equal_filename],
                [a, b, c],
        ):
            with open(filename, "a", encoding="UTF-8") as file:
                print(*list, file=file)
