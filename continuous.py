import math

SEGMENT_SIZE = 1 << 16  # 64 KB window sieved at a time


def prime_stream():
    """Yield primes forever.

    Memory stays roughly constant: one fixed-size window plus the base
    primes up to sqrt(current position), which grow negligibly slowly.
    """
    yield 2
    base = []  # all primes <= base_limit, used to sieve each window
    base_limit = 1
    lo = 3
    while True:
        hi = lo + SEGMENT_SIZE
        root = math.isqrt(hi - 1)
        if root > base_limit:
            # extend the base primes (doubled, so re-extension is rare)
            base_limit = root * 2
            sieve = bytearray([1]) * (base_limit + 1)
            sieve[:2] = b"\x00\x00"
            for i in range(2, math.isqrt(base_limit) + 1):
                if sieve[i]:
                    sieve[i * i :: i] = bytearray(len(range(i * i, base_limit + 1, i)))
            base = [i for i in range(2, base_limit + 1) if sieve[i]]
        window = bytearray([1]) * SEGMENT_SIZE  # window[k] stands for lo + k
        for p in base:
            first = max(p * p, (lo + p - 1) // p * p)  # first multiple in window
            if first >= hi:
                break
            window[first - lo :: p] = bytearray(len(range(first, hi, p)))
        for k in range(SEGMENT_SIZE):
            if window[k]:
                yield lo + k
        lo = hi


if __name__ == "__main__":
    primes = prime_stream()
    next(primes)  # skip 2, matching fast.py's output
    for p in primes:
        print(p)
