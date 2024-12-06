import json
input_filename = input()
output_filename = input()
a = []
with open(input_filename, "r", encoding="UTF-8") as input_file:
    for line in input_file:
        a += [int(x) for x in line.split()]
data = {
    "count": len(a),
    "positive_count": len([x for x in a if x > 0]),
    "min": min(a),
    "max": max(a),
    "sum": sum(a),
    "average": round(sum(a) / len(a), 2),
}
with open(output_filename, "w", encoding="UTF-8") as output_file:
    json.dump(data, output_file, ensure_ascii=False, indent=4)
