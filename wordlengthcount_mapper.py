import sys

def main(separator='\t'):
    """
    Makes key-value pairs with key = word length, value = word count
    """

    for line in sys.stdin:
        for word in line.split():
            print(len(word), separator, 1)

if __name__ == "__main__":
    main()

