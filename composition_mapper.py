import sys

def main(separator='\t'):    
    """
    Makes key-value pairs:
    key = phrase of length equal to provided word composition length, 
    value = phrase count
    """
    # Input composition length from user
    comp_len = int(sys.argv[1])         

    for line in sys.stdin:
        words = line.split()

        # To avoid overshooting index out of bounds
        for i in range(len(words) - comp_len + 1): 
            print(*words[i:i+comp_len], separator, 1)

if __name__ == "__main__":
    main()

