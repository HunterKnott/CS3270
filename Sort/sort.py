'''Hunter Knott, Utah Valley University, CS 2420'''
from random import seed, sample
from time import perf_counter

def quicksort(lyst):
    '''Sorts by using a pivot to divide and deconstruct the list'''
    # There's 1 element, so the list is sorted
    if len(lyst) <= 1:
        return lyst

    # Moves the pivot towards the middle by moving all lowers elements to the left
    pivot_index = 0
    for i in range(1, len(lyst)):
        if lyst[i] <= lyst[0]:
            temp = lyst[i]
            pivot_index += 1
            lyst[i] = lyst[pivot_index]
            lyst[pivot_index] = temp

    lyst[0] = lyst[pivot_index]

    # Sorts the lower and upper halves separately, then combines them
    left_lyst = quicksort(lyst[:pivot_index])
    right_lyst = quicksort(lyst[pivot_index+1:])
    lyst = left_lyst + [lyst[pivot_index]] + right_lyst

    return lyst

def mergesort(lyst):
    '''Sorts by dividing the list down to each element, then recoonstructs it'''
    def merge(left_lyst, right_lyst):
        merged_lyst = []
        i = 0
        j = 0

        # Chooses the lowest from the right/left halves, until one runs out
        while i < len(left_lyst) and j < len(right_lyst):
            if left_lyst[i] < right_lyst[j]:
                merged_lyst.append(left_lyst[i])
                i += 1
            else:
                merged_lyst.append(right_lyst[j])
                j += 1

        # Inserts the rest of the left half elements
        while i < len(left_lyst):
            merged_lyst.append(left_lyst[i])
            i += 1

        # Inserts the rest of right half elements
        while j < len(right_lyst):
            merged_lyst.append(right_lyst[j])
            j += 1

        return merged_lyst

    # There's 1 element, so the list is sorted
    if len(lyst) <= 1:
        return lyst

    #Partitions the full list and recursively sorts each half
    mid = len(lyst) // 2
    left_lyst = mergesort(lyst[0:mid])
    right_lyst = mergesort(lyst[mid:])

    return merge(left_lyst, right_lyst)

def insertion_sort(lyst):
    '''Sorts by having elements step from right to left'''
    for i in range(0, len(lyst)-1):
        j = i
        while (j > 0 and lyst[j] < lyst[j - 1]):
            temp = lyst[j]
            lyst[j] = lyst[j - 1]
            lyst[j - 1] = temp
            j -= 1
    return lyst

def selection_sort(lyst):
    '''Sorts by swapping elements from right to left'''
    for i in range(len(lyst)-1):
        index_smallest = i
        for j in range(i+1, len(lyst)-1):
            if lyst[j] < lyst[index_smallest]:
                index_smallest = j
        temp = lyst[i]
        lyst[i] = lyst[index_smallest]
        lyst[index_smallest] = temp
    return lyst

def is_sorted(lyst):
    '''Checks to see if the list is sorted'''
    if type(lyst) is not list:
        return False
    for i in range(len(lyst) - 1):
        if type(lyst[i]) is not int:
            return False
        if lyst[i] > lyst[i+1]:
            return False
        return True

def main():
    '''Runs various sorting algorithms to test their runtimes'''
    DATA_SIZE = 10000

    # Time for Quicksort algorithm
    seed(0)
    data = sample(range(DATA_SIZE * 3), k = DATA_SIZE)
    test = data.copy()
    print("starting quicksort")
    start = perf_counter()
    test = quicksort(test)
    print("list is sorted:", is_sorted(test))
    end = perf_counter() - start
    print("quicksort duration:", end, "seconds\n")

    # Time for Mergesort algorithm
    seed(0)
    data = sample(range(DATA_SIZE * 3), k = DATA_SIZE)
    test = data.copy()
    print("starting mergesort")
    start = perf_counter()
    test = mergesort(test)
    print("list is sorted:", is_sorted(test))
    end = perf_counter() - start
    print("mergesort duration:", end, "seconds\n")

    # Time for Insertion Sort algorithm
    seed(0)
    data = sample(range(DATA_SIZE * 3), k = DATA_SIZE)
    test = data.copy()
    print("starting insertion_sort")
    start = perf_counter()
    test = insertion_sort(test)
    print("list is sorted:", is_sorted(test))
    end = perf_counter() - start
    print("insertion_sort duration:", end, "seconds\n")

    # Time for Selection Sort algorithm
    seed(0)
    data = sample(range(DATA_SIZE * 3), k = DATA_SIZE)
    test = data.copy()
    print("starting selection_sort")
    start = perf_counter()
    test = selection_sort(test)
    print("list is sorted:", is_sorted(test))
    end = perf_counter() - start
    print("selection_sort duration:", end, "seconds\n")

    # Time for Timsort algorithm
    seed(0)
    data = sample(range(DATA_SIZE * 3), k = DATA_SIZE)
    test = data.copy()
    print("starting timsort")
    start = perf_counter()
    test = sorted(test)
    print("list is sorted:", is_sorted(test))
    end = perf_counter() - start
    print("timsort duration:", end, "seconds\n")

if __name__ == "__main__":
    main()
