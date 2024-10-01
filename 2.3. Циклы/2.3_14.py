n = int(input())
i = 2
r = 'YES'
if n > 1:
    while n % i:
        if i > n ** 0.5:
            break
        i += 1
    else:
        r = 'NO'
else:
    r = 'NO'
print(r)