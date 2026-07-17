import math
import sys

COUNT = 1_000_000  # primes to print: 3, 5, 7, ...

# Upper bound for the (COUNT+1)-th prime (the +1 accounts for 2, which is
# not printed), from Rosser's theorem: p_n < n * (ln n + ln ln n) for n >= 6.
n = COUNT + 1
limit = int(n * (math.log(n) + math.log(math.log(n))))

# Sieve of Eratosthenes: cross out multiples of each prime in bulk.
is_prime = bytearray([1]) * (limit + 1)
is_prime[0] = is_prime[1] = 0
for i in range(2, math.isqrt(limit) + 1):
    if is_prime[i]:
        is_prime[i * i :: i] = bytearray(len(range(i * i, limit + 1, i)))

primes = [i for i in range(3, limit + 1) if is_prime[i]]
sys.stdout.write("\n".join(map(str, primes[:COUNT])) + "\n")
