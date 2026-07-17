Prime_list = [2]


def RecursiveVerify(num: int, prime_list: list, i: int = 0) -> bool:
    # primes are sorted ascending, so once prime_list[i]**2 > num
    # no larger prime can divide it
    if i >= len(prime_list) or prime_list[i] * prime_list[i] > num:
        return True
    elif num % prime_list[i] == 0:
        return False
    else:
        return RecursiveVerify(num, prime_list, i + 1)


for i in range(100000):
    next_num = Prime_list[-1] + 1
    while not RecursiveVerify(next_num, Prime_list):
        next_num += 1
    Prime_list.append(next_num)
    print(Prime_list[-1])