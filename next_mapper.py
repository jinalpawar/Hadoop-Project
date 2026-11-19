#!/usr/bin/env python3

import re
import sys

words = re.compile(r"[^\W\d_]+(?:'[^\W\d_]+)*")
target = sys.argv[1].lower()

prev = None                      
for line in sys.stdin:
    for w in words.findall(line.lower()):
        if prev == target:
            print(f"{w}\t1")
        prev = w
