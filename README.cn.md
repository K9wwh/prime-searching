[English](README.en.md) · **中文**

# prime-searching

五个独立的 Python 素数 (prime number) 生成脚本，从刻意写得很朴素的基线实现，一路到内存恒定的
分段筛 (segmented sieve)。每个脚本都是自包含的（只用标准库 (standard library)，需要
Python 3.8+ —— `oneliner.py` 用了海象运算符 (walrus operator)，`fast.py` 和
`continuous.py` 用了 `math.isqrt`），并把素数逐行打印到标准输出 (stdout)。

按照约定，所有脚本都跳过素数 2、从 3 开始打印，因此它们的输出可以逐行直接对比。

## simple.py — 朴素试除法

对每个候选数 `n`，逐一尝试从 2 到 `sqrt(n)` 的每个除数 `d`。不记住之前找到的素数；
每个候选数都是从零开始检查的。

- **时间 (Time)：** 每个候选数 O(√n)；产生 N 个素数总体大约 O(N·√(N ln N))。
- **空间 (Space)：** O(1)。
- **输出 (Output)：** 100,000 个素数。

```sh
python simple.py
```

## recursive.py — 递归试除法

维护一个不断增长的已找到素数列表，并通过在该列表上递归 (recursion) 来验证每个候选数，
只用平方不超过候选数的那些素数去除。递归取代了通常的循环；递归深度为 π(√n)，
始终保持很小（在这个范围内远低于 Python 的递归深度上限 (recursion limit)）。

- **时间 (Time)：** 每个候选数 O(π(√n)) ≈ O(√n / ln n) 次除法 —— 思路和
  `simple.py` 相同，但只用素数去除。
- **空间 (Space)：** 存储素数列表需要 O(N)，外加 O(π(√n)) 的递归深度。
- **输出 (Output)：** 100,000 个素数。

```sh
python recursive.py
```

## oneliner.py — 海象运算符单行版

整个程序就是一个表达式：一个列表推导式 (list comprehension)，用海象运算符
(`:=`) 反复把 `n` 重新绑定为下一个素数。每一步扫描 `(n, 2n+4)` 区间内的奇数 ——
伯特兰假设 (Bertrand's postulate) 保证该区间内必有素数 —— 并用奇数试除法判定素性。
这是为了代码高尔夫 (code golf) 而写的，不为速度也不为可读性。

- **时间 (Time)：** 每个候选数 O(√n)，与 `simple.py` 同阶。
- **空间 (Space)：** O(N) —— 推导式会先构建出完整列表再打印。
- **输出 (Output)：** 100,000 个素数。

```sh
python oneliner.py
```

## fast.py — 带 Rosser-Schoenfeld 上界的埃拉托斯特尼筛法

根据罗瑟–施恩菲尔德上界 (Rosser-Schoenfeld upper bound)（当 n ≥ 6 时
`p_n < n(ln n + ln ln n)`）算出第 1,000,001 个素数的上限，按该上限（约 1640 万）
分配一个 bytearray，然后用整片切片赋值 (bulk slice assignment) 批量划掉合数 (composite)。
在固定数量的几个脚本里，它快出一大截。

- **时间 (Time)：** 对筛法上限 n 为 O(n log log n)。
- **空间 (Space)：** O(n) —— 上界以内每个数占一个字节。
- **输出 (Output)：** 1,000,000 个素数。

```sh
python fast.py
```

## continuous.py — 分段筛，无限生成器

`prime_stream()` 会永远不断产出素数。它每次只筛一个固定的 64 KB 窗口 (window)，
使用一份惰性扩展 (lazily extended) 的基础素数 (base primes) 列表，覆盖到
`sqrt(current position)`（当前位置的平方根）的 2 倍（每次扩展时上界都取双倍，
因此很少需要重新扩展），所以无论运行多远，内存基本保持恒定。直接运行它，
它会一直打印素数直到被中断。

- **时间 (Time)：** 到位置 n 为止总工作量 O(n log log n)（与普通筛法同阶，
  摊销 (amortized) 到各个窗口上）。
- **空间 (Space)：** 基础素数占 O(√n)，外加那个固定的 64 KB 窗口 ——
  在 n ≈ 10⁹ 附近实际上是几百千字节，且增长慢到可以忽略。
- **输出 (Output)：** 无限；用 Ctrl+C 停止，或通过管道接 `head`。

```sh
python continuous.py            # runs forever
python continuous.py | head -n 100
```

## 对比

| Script        | 算法                              | 打印的素数个数 | 时间（粗略）               | 额外内存             |
|---------------|----------------------------------|----------------|---------------------------|---------------------|
| simple.py     | 朴素试除法                        | 100,000        | 每个候选数 O(√n)           | O(1)                |
| recursive.py  | 递归试除法（只用素数）             | 100,000        | 每个候选数 O(√n / ln n)    | O(N) 素数列表        |
| oneliner.py   | 奇数试除法，单个表达式             | 100,000        | 每个候选数 O(√n)           | O(N) 结果列表        |
| fast.py       | 埃拉托斯特尼筛法                   | 1,000,000      | O(n log log n)            | O(n) bytearray      |
| continuous.py | 分段筛（流式）                     | 无限            | 到 n 为止 O(n log log n)   | 约 O(√n)，实际恒定   |

*n = 所达到素数的量级；N = 产生的素数个数。*

## 许可证

MIT —— 见 [LICENSE](LICENSE)。
