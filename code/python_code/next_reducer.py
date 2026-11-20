#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    """
    Read Mapper output and separate into key and count
    """

    for line in file:
        map_, _, size = line.rstrip().partition(separator)
        yield map_, int(size)

def main(separator='\t'):
    """
    Group mapper output by keys, aggregate by total count weight% across all predicted words
    """

    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    # groupby - group consecutive word-count pairs (sorted mapper output)
    # key - string containing a word/letter
    # group - iterator yielding all [<key>, <count>] items

    total_count = {}
    for key, group in groupby(data, itemgetter(0)):
        total_count[key] = sum(count for _, count in group)
    
    total_count_percent = {k : v * 100/sum(total_count.values()) for k, v in total_count.items()}

    for key, value in total_count_percent.items():
        print(key, separator, value)

if __name__ == "__main__":
    main()