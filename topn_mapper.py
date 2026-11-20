import sys

def main(separator='\t'):
    """
    Makes key-value pairs:
    key = each letter in words with length between 5 to 9 chars, 
    value = letter count
    """

    # input comes from STDIN (standard input)
    for line in sys.stdin:
        words = line.split()

        for word in words:
            # Remove non-alphabetic characters from words (example: Change "N.A.S.A." to "NASA")
            letters = [letter for letter in word if letter.isalpha()]

            if 4 < len(letters) < 10:
                for letter in letters:
                    print(letter, separator, 1)

if __name__ == "__main__":
    main()

