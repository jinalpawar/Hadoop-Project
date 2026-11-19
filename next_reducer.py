#!/usr/bin/env python3

import sys
from collections import Counter

counts = Counter()
for line in sys.stdin:
    word, n = line.rstrip("\n").split("\t")
    counts[word] += int(n)

total = sum(counts.values())
for word, n in counts.most_common():
    print(f"{word}\t{n}\t{100 * n / total:.2f}%")
