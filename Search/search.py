'''Hunter Knott, Utah Valley University, CS 2420'''
from random import seed, sample
from math import sqrt
from time import perf_counter

NUMBER_RANGE = 10000000
LYST_SIZE = 100000

def linear_search(lyst, target):
    '''Searches for a list item by stepping through each element'''
    for i in range(len(lyst)):
        if lyst[i] == target :
            return True # Target was found
    return False # Target wasn't found

def binary_search(lyst, target):
    '''Searches for a list item by dividing the list in half'''
    low = 0
    mid = len(lyst) // 21
    high = len(lyst) - 1

    while high >= low:
        mid = (high + low) // 2

        if lyst[mid] < target:
            low = mid + 1

        elif lyst[mid] >  target:
            high = mid - 1

        else:
            return True # Target was found

    return False # Target wasn't found

def jump_search(lyst, target):
    '''Searches for a list item by searching through list intervals'''
    interval = int(sqrt(len(lyst))) # Number of elements per jump
    current_index = interval

    while current_index < len(lyst):
        if lyst[current_index] < target: # Target not in interval range
            if (len(lyst) - 1) - current_index <= interval: # If algorithm is on the last step
                return linear_search(lyst[current_index:], target)
            else: # If algorithm has more steps to go
                current_index = current_index + interval

        elif lyst[current_index] > target: # Target in interval range, so walk through range
            return linear_search(range(lyst[current_index - interval], lyst[current_index]), target)

        else:
            return False # Target wasn't found

def main():
    '''Tests runtimes of various searching algorithms'''
    # Create a list of random numbers and sort it
    seed(0)
    lyst = sample(range(NUMBER_RANGE), LYST_SIZE)
    lyst.sort()

    first_value = lyst[0]
    middle_value = lyst[(LYST_SIZE - 1) // 2]
    last_value = lyst[-1]

    # Times for Linear Search algorithm
    linear_search(lyst, first_value)
    stop = perf_counter()
    print("Elapsed time of Linear Search for first value:", stop, "seconds")

    linear_search(lyst, middle_value)
    stop = perf_counter()
    print("Elapsed time of Linear Search for middlevalue:", stop, "seconds")

    linear_search(lyst, last_value)
    stop = perf_counter()
    print("Elapsed time of Linear Search for last value:", stop, "seconds")

    linear_search(lyst, -1)
    stop = perf_counter()
    print("Elapsed time of Linear Search for non-existent value:", stop, "seconds")

    # Times for Binary Search algorithm
    binary_search(lyst, first_value)
    stop = perf_counter()
    print("Elapsed time of Binary Search for first value:", stop, "seconds")

    binary_search(lyst, middle_value)
    stop = perf_counter()
    print("Elapsed time of Binary Search for middlevalue:", stop, "seconds")

    binary_search(lyst, last_value)
    stop = perf_counter()
    print("Elapsed time of Binary Search for last value:", stop, "seconds")

    binary_search(lyst, -1)
    stop = perf_counter()
    print("Elapsed time of Binary Search for non-existent value:", stop, "seconds")

    # Times for Jump Search algorithm
    jump_search(lyst, first_value)
    stop = perf_counter()
    print("Elapsed time of Jump Search for first value:", stop, "seconds")

    jump_search(lyst, middle_value)
    stop = perf_counter()
    print("Elapsed time of Jump Search for middlevalue:", stop, "seconds")

    jump_search(lyst, last_value)
    stop = perf_counter()
    print("Elapsed time of Jump Search for last value:", stop, "seconds")

    jump_search(lyst, -1)
    stop = perf_counter()
    print("Elapsed time of Jump Search for non-existent value:", stop, "seconds")

if __name__ == '__main__':
    main()