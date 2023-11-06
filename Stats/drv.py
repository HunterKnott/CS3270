# '''Hunter Knott and Aarron Rasmussen, ECE 3710, Utah Valley University'''

# Problem 1.
# Discrete Random Variable 
# P(X=1) = 0.3, P(X=0) = 0.7
# Probability Mass Function: f(x) = P^x (1-P)^(1-x)
# This is a Bernoulli Distribution

import numpy as np
import matplotlib.pyplot as plt

prob_1 = 0.3
pmf = [1-prob_1, prob_1]

# a. Find the mean (expected value) of X using the given pmf
def mean(function):
    return sum(prob * index for index, prob in enumerate(function))

m = mean(pmf)
print('PMF Mean: ' + str(m))

# b. Find the variance of the random variable X using the given pmf.
def variance(function):
    return sum((index - m)**2 * prob for index, prob in enumerate(function))

v = variance(pmf)
v = round(v, 2)
print('PMF Variance: ' + str(v))

# c. Now the engineer/scientist, starts measuring the output. He/she repeats the process 20 times. The outcomes are as follows:
output = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0]

# c-1. Plot the histogram of data
bin_edges = [0, 1, 2, 2]
plt.hist(output, bins=bin_edges, rwidth=1, color='#deac57', alpha=0.8, edgecolor='black')
plt.xticks([0, 1])

# Set the labels and title
plt.xlabel('Output Reading')
plt.ylabel('Frequency')
plt.title('Histogram of IC Pin Outputs (c-1)')

plt.show()

# c-2. Normalize the histogram and plot it.
bin_edges = [0, 1, 2]
plt.hist(output, bins=bin_edges, rwidth=1, color='#3bb351', alpha=0.8, edgecolor='black', density=True)
plt.xticks([0, 1])

# Set the labels and title
plt.xlabel('Output Reading')
plt.ylabel('Frequency Percentage')
plt.title('Normalized Histogram of IC Pin Outputs (c-2)')
plt.ylim(0, 1)

plt.show()

# c-3. Find the mean and variance of the collected samples. Find the probability of p(X=1) from the
# collected measurements (is this the same as the actual probability P?). Compare the results with the actual
# mean and variances. Are they different? Explain what you learned from this problem.
def sample_mean(sample):
    return sum(sample) / len(sample)

def sample_variance(sample, s_mean):
    squared_differences = [(x - s_mean) ** 2 for x in sample]
    sample_variance = sum(squared_differences) / (len(sample) - 1)
    return sample_variance

m2 = sample_mean(output)
print('Sample Output Mean: ' + str(m2))

v2 = sample_variance(output, m2)
v2 = round(v2, 3)
print('Sample Output Variance: ' + str(v2))

freq_0 = output.count(0) / len(output)
freq_1 = output.count(1) / len(output)
frequencies = [freq_0, freq_1]
print('Output probability of 0: ' + str(freq_0))
print('Output probability of 1: ' + str(freq_1))

# According to the results printed out, there's a slight difference between the PMF Mean/Variance
# and the sample Mean/Variance. This is because the PMF was expecting 70% of data to be 0's and
# the other 30% to be ones. In the case of the sample data, 65% was 0's and 35% was 1's.
# This shows that taking samples is good for an approximation, but usually doesn't match the
# original PMF probabilites exactly. Although the larger the sample becomes, there's usually
# more of a likelihood that it will approach the true mean/variance values.

# c-4) Plot the data with the approximated pmf (look at the actual pmf and instead of P use the probability
# of p(X=1) you found from the data). Plot the approximated and the actual pmf.

# PMF plot for approximated PMF
plt.figure(figsize=(10, 4)) 
plt.subplot(1, 2, 1) 
plt.bar([0, 1], frequencies, color='#b55959', edgecolor='black')
plt.xticks([0, 1], ['0', '1'])
plt.xlabel("Output")
plt.ylabel("Probability")
plt.title("Approximated Probability Mass Function (c-4)")

# PMF plot for actual PMF
plt.subplot(1, 2, 2)
plt.bar([0, 1], pmf, color='#6ba4d6', edgecolor='black') 
plt.xticks([0, 1], ['0', '1'])
plt.xlabel("Output")
plt.ylabel("Probability")
plt.title("Actual Probability Mass Function (c-4)")

plt.tight_layout()
plt.show()

# ______________________________________________________________________________________________
# Problem 2

# import matplotlib.pyplot as plt
# import numpy as np
# from itertools import repeat

# def find_sample_mean(data_list):
#     return np.mean(data_list)

# def find_sample_variance(data_list):
#     return np.var(data_list)

# def gaussian_pdf(d, mean, variance):
#     return 1 / (np.sqrt(2 * np.pi * variance)) * np.exp(-(d - mean)**2 / (2 * variance))

# if __name__ == '__main__':
#     data = [201.4579, 200.9891, 207.9385, 195.9777, 203.4831, 204.1754, 198.7814, 201.0784, 194.1708,
#             194.2602, 200.5244, 203.6113, 212.9275, 196.6655, 200.9367, 199.5875, 190.3349, 197.8052,
#             191.0266, 204.2019]

#     # question a: find mean and variance of the data
#     sample_mean = find_sample_mean(data)
#     sample_variance = find_sample_variance(data)

#     print(f"sample mean: {sample_mean}")
#     print(f"sample variance: {sample_variance}")

#     # question b: write down the pdf of data based on the mean, variance and the given pdf
#     print(f"equation: 1/(sqrt(2 * pi * {sample_variance})) * e^(- (x - {sample_mean}^2 / (2 * {sample_variance})))")

#     # question c: plot the histogram of data with bin size 5
#     histogram = plt.hist(data, 5)
#     plt.show()

#     # question d: plot the pdf on the equation given for f(x)
#     x = np.arange(180, 220.01, 0.01)
#     results = list(map(gaussian_pdf, x, repeat(sample_mean), repeat(sample_variance)))

#     histogram_two = plt.plot(x, results)
#     plt.show()

    # question e:
    # Python and Matlab are very useful for making continuous graphs given an equation, not just
    # discrete graphs that use bars. It can be difficult to correctly format the equations in
    # your code due to all the pieces and exponents you have to remember though. I also learned
    # how useful the e variable is with making graphs. It seems like an arbitrary number that
    # doesn't make much sense sometimes, but it really helps illustrate how useful it is when
    # you use it in a graph equation.