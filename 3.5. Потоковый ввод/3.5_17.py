with open("secret.txt", "r", encoding="UTF-8") as file:
    f = file.read()
    for i in f:
        print(chr(ord(i) % 128), end="")
