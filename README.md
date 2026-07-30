# prime-searching

Five standalone Python scripts that generate prime numbers, from a deliberately naive
baseline to a constant-memory segmented sieve. Each script is self-contained (standard
library only, Python 3.8+) and prints one prime per line to stdout. By convention all
scripts skip the prime 2 and start printing at 3, so their outputs are directly
comparable line-by-line.

五个独立的 Python 素数生成脚本，从刻意写得很朴素的基线实现，一路到内存恒定的分段筛。
每个脚本都是自包含的（只用标准库，需要 Python 3.8+），并把素数逐行打印到标准输出。
按照约定，所有脚本都跳过素数 2、从 3 开始打印，因此它们的输出可以逐行直接对比。

```sh
python simple.py        # naive trial division      / 朴素试除法
python recursive.py     # recursive trial division  / 递归试除法
python oneliner.py      # walrus one-liner          / 海象运算符单行版
python fast.py          # sieve of Eratosthenes     / 埃拉托斯特尼筛法
python continuous.py    # segmented sieve, infinite / 分段筛，无限生成
```

📖 **Docs:** [English](README.en.md) · [中文](README.cn.md)

License: MIT — see [LICENSE](LICENSE).
