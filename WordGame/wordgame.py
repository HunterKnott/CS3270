'''Hunter Knott, CS 3270, Utah Valley University'''
from itertools import groupby # Use to sort permutations by length
import random
from collections import Counter # Use when checking for subset words

def read_words(file_name):
    try:
        with open(file_name, 'r') as word_file:
            lines = [line.strip() for line in word_file.readlines()]
    except FileNotFoundError:
        print('The file ' + str(file_name) + ' does not exist')
    return lines

def main(length_range = None):
    if length_range:
        min_length, max_length = map(int, length_range.split(','))
    else:
        min_length, max_length = 3, 15 # Default range

    words = read_words('words.txt')
    filter_words = [w for w in words if min_length <= len(w) <= max_length]
    word = random.choice(filter_words)
    word_chars = list(word)

    # sub_words = []
    # for w in words:
    #     is_sub = True
    #     word_char_copy = word_chars.copy()
    #     for c in w:
    #         if c in word_char_copy:
    #             word_char_copy.remove(c)
    #         else:
    #             is_sub = False
    #     if is_sub and min_length <= len(w) <= max_length:
    #         sub_words.append(w)

    from collections import Counter 
    sub_words = []
    word_counter = Counter(word_chars)
    for w in words:
        w_counter = Counter(w)
        if all(w_counter[c] <= word_counter[c] for c in w) and min_length <= len(w) <= max_length:
            sub_words.append(w)

    sub_words.sort(key=len)
    sub_words_grouped = {key: list(group) for key, group in groupby(sub_words, key=len)}

    # Print all permutations
    print(f'The word is {word}')
    for length, words_group in sub_words_grouped.items():
        print(f'Words of length {length}:')
        [print(word) for word in words_group]
    
    # Print scrambled word
    random.shuffle(word_chars)
    print('\n' + ''.join(word_chars) + ':\n')
    
    # Print word spaces
    for length, words_group in sub_words_grouped.items():
        print('[' + ', '.join(["'" + '-' * length + "'" for word in words_group]) + ']')
    
    print(sub_words)
    guess = input('\nEnter a guess: ')

if __name__ == "__main__":
    length_range = input("Enter the range for word length (min, max): ")
    main(length_range)