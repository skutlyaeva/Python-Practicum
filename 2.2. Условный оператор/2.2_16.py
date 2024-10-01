s1 = int(input())
s2 = int(input())
s3 = int(input())
if s1 > s2 and s1 > s3:
    if s2 > s3:
        print("          Петя          ")
        print("  Вася  ")
        print("                  Толя  ")
        print("   II      I      III   ")
    else:
        print("          Петя          ")
        print("  Толя  ")
        print("                  Вася  ")
        print("   II      I      III   ")
if s2 > s1 and s2 > s3:
    if s1 > s3:
        print("          Вася          ")
        print("  Петя   ")
        print("                  Толя  ")
        print("   II      I      III   ")
    else:
        print("          Вася          ")
        print("  Толя   ")
        print("                  Петя  ")
        print("   II      I      III   ")
if s3 > s1 and s3 > s2:
    if s1 > s2:
        print("          Толя          ")
        print("  Петя   ")
        print("                  Вася  ")
        print("   II      I      III   ")
    if s2 > s1:
        print("          Толя          ")
        print("  Вася   ")
        print("                  Петя  ")
        print("   II      I      III   ")