input_filename = input()
output_filename = input()
with open(input_filename, "r", encoding="UTF-8") as input_file:
    with open(output_filename, "w", encoding="UTF-8") as output_file:
        for line in input_file:
            line = line.strip().replace("\t", "")
            a = line.split()
            if len(a) != 0:
                print(*a, file=output_file)
