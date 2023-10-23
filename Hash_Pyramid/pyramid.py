'''Hunter Knott, Utah Valley University, CS 2420'''
import sys
from time import perf_counter
from hashmap import HashMap

cache = HashMap()
keys_list = []
calls = 0
cache_hits = 0

def weight_on(r, c):
    '''Calculates and caches pyramid node weights'''
    global keys_list
    global cache
    keys_list = cache.keys()
    node_weight = weight_helper(r, c)
    if (r,c) not in keys_list and r >= 0 and c >= 0:
        cache.set((r,c), node_weight)
    return node_weight

def weight_helper(r, c):
    '''Recursively calculates a pyramid node weight'''
    global keys_list
    global calls
    global cache_hits
    calls += 1
    second_weight = 200
    if c-1 < 0 or c > r-1:
        second_weight = 0
    if c < 0  or c > r or r <= 0:
        return 0
    else:
        keys_list = cache.keys()
        # Comment out this if block to test part 2
        if (r,c) in keys_list:
            cache_hits += 1
            return cache.get((r,c))
        left_weight = weight_on(r-1, c-1)
        right_weight = weight_on(r-1, c)
        return (200 + second_weight + left_weight + right_weight)/2

def display_pyramid():
    '''Creates and returns a string of all pyramid node weights'''
    pyramid_string = ""
    height = int(sys.argv[1])
    for r in range(height):
        for c in range(r + 1):
            pyramid_string += ' ' + f'{weight_on(r, c):.2f}'
        pyramid_string += '\n'
    return pyramid_string

def main():
    '''Calculates and displays the weight distrubution of a human pyramid'''
    # with open('part2.txt', 'w') as f:
    #     f.write(display_pyramid())
    #     f.write("Elapsed time: " + str(perf_counter()) + " seconds")
    #     f.write('\n' + "Number of function calls: " + str(calls))
    #     f.write('\n' + "Number of cache hits: " + str(cache_hits))

    print(display_pyramid())
    print("Elapsed time: " + str(perf_counter()) + " seconds")
    print('\n' + "Number of function calls: " + str(calls))
    print('\n' + "Number of cache hits: " + str(cache_hits))

if __name__ == "__main__":
    main()
