a = input(), input()
output_filename = input()
b = []
for input_filename in a:
    word_set = set()
    with open(input_filename, "r", encoding="UTF-8") as input_file:
        for line in input_file:
            word_set.update(line.split())
    b.append(word_set)
with open(output_filename, "w", encoding="UTF-8") as output_file:
    for word in sorted(b[0].symmetric_difference(b[1])):
        print(word, file=output_file)