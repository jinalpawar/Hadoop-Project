#!/usr/bin/env python3

import re
import sys

target = sys.argv[1]
pattern = re.compile(r"(?<![\w'])" + re.escape(target) + r"(?![\w'])", re.IGNORECASE)

text = re.sub(r"\s+", " ", sys.stdin.read())
for sentence in re.split(r"(?<=[.!?])\s+", text):
    if pattern.search(sentence):
        print(sentence.strip())
