'''Hunter Knott, CS 3270, Utah Valley University'''
from itertools import groupby # Use to sort permutations by length
from random import choice, shuffle
from collections import Counter # Use when checking subsets

def read_words(file_name):
    try:
        with open(file_name, 'r') as word_file:
            lines = [line.strip() for line in word_file.readlines()]
    except FileNotFoundError:
        print('The file ' + str(file_name) + ' does not exist')
    return lines

def main(length_range = None):
    words = read_words('words.txt')
    if length_range:
        min_length, max_length = map(int, length_range.split(','))
    else:
        min_length, max_length = 3, 15 # Default range
    
    word = ' '

if __name__ == "__main__":
    # input_word = input("Enter the range for word length (min, max): ")
    # main(length_range)
    main()