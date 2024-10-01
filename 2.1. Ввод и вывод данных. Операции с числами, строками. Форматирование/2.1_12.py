a = input()
b = input()
a1 = f'{a:0>3}'
b1 = f'{b:0>3}'
s1 = str(int(a1[0]) + int(b1[0]))[-1]
s2 = str(int(a1[1]) + int(b1[1]))[-1]
s3 = str(int(a1[2]) + int(b1[2]))[-1]
print(int(s1 + s2 + s3))