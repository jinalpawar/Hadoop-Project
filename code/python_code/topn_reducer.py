from itertools import groupby
from operator import itemgetter
from math import ceil
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
    Group mapper output by keys, aggregate by total count, print only top n% of used letters
    """
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    top_n = {}

    # groupby - group consecutive word-count pairs (sorted mapper output)
    # key - string containing a word/letter
    # group - iterator yielding all [<key>, <count>] items

    for key, group in groupby(data, itemgetter(0)):
        top_n[key] = sum(int(count) for _, count in group)

    # select top n% of letters from selected words 
    n = ceil((int(sys.argv[1])/100) * len(top_n))

    # sort by count and make list of tuples
    sorted_letters = sorted(top_n.items(), key=lambda item: item[1], reverse=True) 

    for l, c in sorted_letters[:n]:
        print(l, c, sep=separator)

if __name__ == "__main__":
    main()