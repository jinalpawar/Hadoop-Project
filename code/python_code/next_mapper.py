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

def main(separator='\t'):    
    """
    Makes key-value pairs:
    key = prediction-word IF previous word = given word, 
    value = prediction-word count
    """
    # input target word from user
    target = sys.argv[1].lower()
    prev = None

    for line in sys.stdin:
        words = line.split()

        for word in words:
            # check word at index n-1
            if prev == target:

                # print word at index n
                print(word, separator, 1)

            prev = word


if __name__ == "__main__":
    main()


