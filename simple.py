def is_prime(n: int) -> bool:
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


count = 0
n = 3
while count < 100000:
    if is_prime(n):
        print(n)
        count += 1
    n += 1
