a = int(input())
m = ""
with open("public.txt", "r", encoding="UTF-8") as file:
    s = file.read()
    for i in s:
        if 65 <= ord(i) <= 90:
            m += chr(65 + (ord(i) - 65 + a) % (90 - 65 + 1))
        elif 97 <= ord(i) <= 122:
            m += chr(97 + (ord(i) - 97 + a) % (122 - 97 + 1))
        else:
            m += i
with open("private.txt", "w") as file_out:
    print(m, file=file_out)