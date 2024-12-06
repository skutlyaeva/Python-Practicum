with open("numbers.num", "rb") as file:
    data = file.read()
r = 0
for i in range(0, len(data), 2):
    r += int.from_bytes(data[i: i + 2], "big")
r = r % 2 ** 16
print(r)