def is_prime(n):
    if n < 2:
        return False

    b = 2
    while b <= n ** 0.5:
        if n % b == 0:
            return False
        b += 1
    return True