'''Hunter Knott, ECE 3710, Utah Valley University'''
from math import sqrt

method_A = [18.0, 18.0, 19.0, 20.0, 21.0, 22.0, 22.5, 23.3, 24.0, 24.0, 24.5, 25.0, 25.0, 25.4, 26.2, 26.4]

method_B = [18.6, 18.9, 19.2, 19.6, 20.1, 20.3, 20.4, 20.4, 20.5, 20.6, 21.2, 22.0, 22.0, 22.3, 22.5, 23.6]

# a. Compute the mean of the entries for each method.
def average(entries):
    return round(sum(entries) / len(entries), 1)

# b. Compute the median of the entries for each method.
def median(entries):
    if len(entries) % 2 == 1:
        return entries[len(entries) // 2]
    else:
        first = entries[len(entries) // 2 - 1]
        second = entries[len(entries) // 2]
        return (first + second) / 2

# c. Compute the first and third quartiles for each method.
def Q1(entries):
    if len(entries) % 2 == 1:
        return entries[((len(entries) + 1) // 4) - 1]
    else:
        first = entries[((len(entries) + 1) // 4) - 1]
        second = entries[(len(entries) + 1) // 4]
        return (first + second) / 2

def Q3(entries):
    if len(entries) % 2 == 1:
        return entries[(3 * (len(entries) + 1) // 4) - 1]
    else:
        first = entries[(3 * (len(entries) + 1) // 4) - 1]
        second = entries[3 * (len(entries) + 1) // 4]
        return (first + second) / 2

# d. Compute the standard deviation of the entries for each method.
def variance(entries):
    squared_sum = sum((e - average(entries)) ** 2 for e in entries)
    return squared_sum / (len(entries) - 1)

def sta_dev(entries):
    return round(sqrt(variance(entries)), 1)

def main():
    print('Average of mA: ' + str(average(method_A)))
    print('Average of mB: ' + str(average(method_B)))

    print('Median of mA: ' + str(median(method_A)))
    print('Median of mB: ' + str(median(method_B)))

    print('First Quartile of mA: ' + str(Q1(method_A)))
    print('First Quartile of mB: ' + str(Q1(method_B)))

    print('Third Quartile of mA: ' + str(Q3(method_A)))
    print('Third Quartile of mB: ' + str(Q3(method_B)))

    print('Standard Deviation of mA: ' + str(sta_dev(method_A)))
    print('Standard Deviation of mB: ' + str(sta_dev(method_B)))

if __name__ == '__main__':
    main()