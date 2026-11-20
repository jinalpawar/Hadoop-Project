import sys

def main():
    """
    Preprocess text to keep one sentence per line
    """

    input_path = sys.argv[1]
    output_name = "text_processed.txt"

    sentences = []

    with open(input_path, 'r') as file: 
        content = file.readlines()
        para = ''.join(content)

    sentences = para.replace("\n", " ").replace("\t", " ").strip().lower().split(". ")

    with open(output_name, 'w') as output:
        output.writelines(sentences)

if __name__ == "__main__":
    main()
