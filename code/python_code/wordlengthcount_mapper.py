import sys

def main(separator='\t'):
    """
    Makes key-value pairs: 
    key = word length, 
    value = word count
    """

    for line in sys.stdin:
        for word in line.split():
            print(len(word), 1, sep=separator)

if __name__ == "__main__":
    main()