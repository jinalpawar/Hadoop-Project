#!/usr/bin/env python3

import sys

def main(separator='\t'):    
    """
    Makes key-value pairs:
    key = sentence containing given word, 
    value = sentence count
    """
    # input target word from user
    target = sys.argv[1].lower()

    for line in sys.stdin:
        words = line.split()

        if target in words:
            print(line, separator, 1)


if __name__ == "__main__":
    main()