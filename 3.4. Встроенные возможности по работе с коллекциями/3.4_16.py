from itertools import chain, permutations, product
a = input().strip()
b = input().strip()
suits = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
ranks = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']
ranks.remove(b)
w = product(ranks, suits.values())
triplets = permutations(w, 3)
triplets = [i for i in triplets if suits[a] in chain.from_iterable(i)]
sorted_combinations = sorted(triplets)
for u in sorted_combinations[:10]:
    print(', '.join(f'{i} {j}' for i, j in u))