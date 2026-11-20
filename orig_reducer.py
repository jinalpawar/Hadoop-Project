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
    Groups mapper output by keys, aggregate by total count
    """

    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    # groupby - group consecutive word-count pairs of sorted mapper output
    # key - string containing a word/letter
    # group - iterator yielding all [<key>, <count>] items

    for key, group in groupby(data, itemgetter(0)):

        total_count = sum(count for _, count in group)
        print(key, separator, total_count)


if __name__ == "__main__":
    main()