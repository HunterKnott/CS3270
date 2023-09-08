'''Hunter Knott, ECE 3710, Utah Valley University'''
# Question 1
from math import sqrt
import numpy as np
import matplotlib.pyplot as graph
import statistics
import random

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

method_A = [18.0, 18.0, 19.0, 20.0, 21.0, 22.0, 22.5, 23.3, 24.0, 24.0, 24.5, 25.0, 25.0, 25.4, 26.2, 26.4]
method_B = [18.6, 18.9, 19.2, 19.6, 20.1, 20.3, 20.4, 20.4, 20.5, 20.6, 21.2, 22.0, 22.0, 22.3, 22.5, 23.6]

# Display
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


# # Question 2
sample = [2099, 528, 2030, 1350, 1018, 384, 1499, 1265, 375, 424,
            789, 810, 522, 513, 488, 200, 215, 486, 257, 557, 260, 461, 500]
sample = sorted(sample)

# a. Construct a boxplot
graph.boxplot(sample)
graph.title('Sample Boxplot')
graph.ylabel('Sample Values')
graph.show()

# b. Construct a histogram and normalized histogram
# 2030 and 2099 are outliers on the boxplot
graph.hist(sample, bins=10, label='Histogram', edgecolor='k')
graph.title('Sample Histogram and Normal Distribution')
graph.xlabel('Value')
graph.ylabel('Frequency')
graph.show()

mean = np.mean(sample)
std_dev = np.std(sample)
normal_dist = np.random.normal(mean, std_dev, 1000)
graph.hist(normal_dist, bins=10, label='Normal Distribution', color='g', edgecolor='k')
graph.xlabel('Value')
graph.ylabel('Frequency')
graph.show()

# Question 3
children_data = [0] * 27 + [1] * 22 + [2] * 30 + [3] * 12 + [4] * 7 + [5] * 2

# a. Find the sample mean of the number of children
def sample_average(entries):
    return round(sum(entries) / len(entries), 1)

# b. Find the sample standard deviation of the number of children
def sample_variance(entries):
    squared_sum = sum((e - sample_average(entries)) ** 2 for e in entries)
    return squared_sum / (len(entries) - 1)

def sample_std_dev(entries):
    return round(sqrt(sample_variance(entries)), 1)

# c. Find the sample median of the number of children
def sample_median(entries):
    if len(entries) % 2 == 1:
        return entries[len(entries) // 2]
    else:
        first = entries[len(entries) // 2 - 1]
        second = entries[len(entries) // 2]
        return (first + second) / 2

# d. Find the first quartile of the number of children
def sample_Q1(entries):
    if len(entries) % 2 == 1:
        return entries[((len(entries) + 1) // 4) - 1]
    else:
        first = entries[((len(entries) + 1) // 4) - 1]
        second = entries[(len(entries) + 1) // 4]
        return (first + second) / 2

# Display
print('Sample Mean: ' + str(sample_average(children_data)))
print('Sample Standard Deviation: ' + str(sample_std_dev(children_data)))
print('Sample Median: ' + str(sample_median(children_data)))
print('Sample First Quartile: ' + str(sample_Q1(children_data)))