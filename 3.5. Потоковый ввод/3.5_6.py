dict = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ъ": "",
    "Ы": "Y",
    "Ь": "",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
}

input_filename = "cyrillic.txt"
output_filename = "transliteration.txt"
a = []
b = []
with open(input_filename, "r", encoding="UTF-8") as input_file:
    for line in input_file:
        a.append(line.strip())
for line in a:
    output_line = ""
    for i in line:
        if i.upper() in dict.keys():
            if i.upper() == i:
                output_line += dict[i].lower().capitalize()
            else:
                output_line += dict[i.upper()].lower()
        else:
            output_line = output_line + i
    b.append(output_line)
with open(output_filename, "w", encoding="UTF-8") as output_file:
    print(*b, sep="\n", file=output_file)
