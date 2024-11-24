from itertools import product
a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
b = ['пик', 'треф', 'бубен', 'червей']
b.remove(input())
for i in product(a, b):
    print(i[0], i[1])
