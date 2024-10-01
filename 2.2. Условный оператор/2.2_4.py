s1 = int(input())
s2 = int(input())
s3 = int(input())
if s1 > s2 and s1 > s3:
    if s2 > s3:
        print("1. Петя")
        print("2. Вася")
        print("3. Толя")
    else:
        print("1. Петя")
        print("2. Толя")
        print("3. Вася")
if s2 > s1 and s2 > s3:
    if s1 > s3:
        print("1. Вася")
        print("2. Петя")
        print("3. Толя")
    else:
        print("1. Вася")
        print("2. Толя")
        print("3. Петя")
if s3 > s1 and s3 > s2:
    if s1 > s2:
        print("1. Толя")
        print("2. Петя")
        print("3. Вася")
    if s2 > s1:
        print("1. Толя")
        print("2. Вася")
        print("3. Петя")
