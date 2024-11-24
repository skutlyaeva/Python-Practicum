from itertools import chain, combinations, product
a = input().strip()
b = input().strip()
c = input()
suits = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
ranks = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']
ranks.remove(b)
w = product(ranks, suits.values())
triplets = combinations(w, 3)
triplets = [i for i in triplets if suits[a] in chain.from_iterable(i)]
triplets.sort()
print_next = False
for triplet in triplets:
    if print_next:
        print(', '.join(f'{i} {j}' for i, j in triplet))
        break
    if ', '.join(f'{i} {j}' for i, j in triplet) == c:
        print_next = True