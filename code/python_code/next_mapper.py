import re
import sys

words = re.compile(r"[^\W\d_]+(?:'[^\W\d_]+)*")
target = sys.argv[1].lower()

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
                print(word, 1, sep=separator)

            prev = word


if __name__ == "__main__":
    main()