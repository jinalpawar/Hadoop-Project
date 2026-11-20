import sys

def main():
    """
    Preprocess text to keep one sentence per line
    """

    for para in sys.stdin:
        # Remove trailing new line characters and periods
        # Lowercase all words
        # Split on period. This fails the case for abbreviations
        
        sentences = para.rstrip("\n").rstrip(".").lower().split(". ")

        print(*sentences, sep="\n")

if __name__ == "__main__":
    main()
