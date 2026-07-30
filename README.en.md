**English** · [中文](README.cn.md)

# prime-searching

Five standalone Python scripts that generate prime numbers, from a deliberately
naive baseline to a constant-memory segmented sieve. Each script is
self-contained (standard library only, Python 3.8+ — `oneliner.py` for the
walrus operator, `fast.py` and `continuous.py` for `math.isqrt`) and prints one
prime per line to stdout.

By convention, all scripts skip the prime 2 and start printing at 3, so their
outputs are directly comparable line-by-line.

## simple.py — naive trial division

Tests each candidate `n` by trying every divisor `d` from 2 up to `sqrt(n)`.
No memory of previous primes; every candidate is checked from scratch.

- **Time:** O(√n) per candidate, roughly O(N·√(N ln N)) overall for N primes.
- **Space:** O(1).
- **Output:** 100,000 primes.

```sh
python simple.py
```

## recursive.py — recursive trial division

Keeps a growing list of found primes and verifies each candidate by recursing
through that list, dividing only by primes whose square does not exceed the
candidate. The recursion replaces the usual loop; depth is π(√n), which stays
small (well under Python's recursion limit for this range).

- **Time:** O(π(√n)) ≈ O(√n / ln n) divisions per candidate — the same idea as
  `simple.py` but dividing only by primes.
- **Space:** O(N) for the stored prime list, plus O(π(√n)) recursion depth.
- **Output:** 100,000 primes.

```sh
python recursive.py
```

## oneliner.py — walrus one-liner

The whole program is a single expression: a list comprehension that repeatedly
rebinds `n` with the walrus operator (`:=`) to the next prime. Each step scans
the odd numbers in `(n, 2n+4)` — Bertrand's postulate guarantees a prime in
that range — and checks primality by odd trial division. Written for golf, not
speed or readability.

- **Time:** O(√n) per candidate, same order as `simple.py`.
- **Space:** O(N) — the comprehension builds the full list before printing.
- **Output:** 100,000 primes.

```sh
python oneliner.py
```

## fast.py — Sieve of Eratosthenes with Rosser-Schoenfeld bound

Computes a limit for the 1,000,001st prime from the Rosser-Schoenfeld upper
bound (`p_n < n(ln n + ln ln n)` for n ≥ 6), allocates one bytearray up to that
bound (~16.4 million), and crosses out composites with bulk slice
assignments. Fastest of the fixed-count scripts by a wide margin.

- **Time:** O(n log log n) for the sieve limit n.
- **Space:** O(n) — one byte per number up to the bound.
- **Output:** 1,000,000 primes.

```sh
python fast.py
```

## continuous.py — segmented sieve, infinite generator

`prime_stream()` yields primes forever. It sieves one fixed 64 KB window at a
time using a lazily-extended list of base primes up to twice `sqrt(current
position)` (the bound is doubled on each extension, so re-extension is rare),
so memory stays effectively constant no matter how far it runs.
Run it directly and it prints primes until interrupted.

- **Time:** O(n log log n) total work up to position n (same order as the
  plain sieve, amortized across windows).
- **Space:** O(√n) for the base primes plus the fixed 64 KB window — in
  practice a few hundred kilobytes around n ≈ 10⁹, growing negligibly slowly.
- **Output:** infinite; stop with Ctrl+C or pipe through `head`.

```sh
python continuous.py            # runs forever
python continuous.py | head -n 100
```

## Comparison

| Script        | Algorithm                        | Primes printed | Time (rough)              | Extra memory        |
|---------------|----------------------------------|----------------|---------------------------|---------------------|
| simple.py     | Naive trial division             | 100,000        | O(√n) per candidate       | O(1)                |
| recursive.py  | Recursive trial division (primes only) | 100,000  | O(√n / ln n) per candidate | O(N) prime list    |
| oneliner.py   | Odd trial division, one expression | 100,000      | O(√n) per candidate       | O(N) result list    |
| fast.py       | Sieve of Eratosthenes            | 1,000,000      | O(n log log n)            | O(n) bytearray      |
| continuous.py | Segmented sieve (streaming)      | infinite       | O(n log log n) up to n    | ~O(√n), effectively constant |

*n = magnitude of the primes reached; N = count of primes produced.*

## License

MIT — see [LICENSE](LICENSE).
