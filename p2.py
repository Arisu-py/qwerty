def is_prime(n):
    if n < 2:
        return 'NO'
    elif n / 2 == 2:
        return 'NO'
    for divisor in range(2, n // 2 + 1):
        if n % divisor == 0:
            return 'NO'
    return 'YES'


print(is_prime(int(input())))
