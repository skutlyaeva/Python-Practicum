s = input()
print(f'a b c f')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int(eval(s, {'a': a, 'b': b, 'c': c}))
            print(f'{a} {b} {c} {f}')
