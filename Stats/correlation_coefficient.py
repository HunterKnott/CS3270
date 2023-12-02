'''Hunter Knott, ECE 3710, Utah Valley University'''
# Problem 2
# A chemical engineer is studying the effect of temperature and stirring rate on the yield of
# a certain product. The process is run 16 times, at the settings indicated in the following table.
# The units for yield are percent of a theoretical maximum.

import math

def correlation_coefficient(x, y):
    n = len(x)
    x_sum = sum(x)
    y_sum = sum(y)

    xy = [x * y for x, y in zip(x, y)]
    xy_sum = sum(xy)

    x_squared = [num**2 for num in x]
    x_squared_sum = sum(x_squared)

    y_squared = [num**2 for num in y]
    y_squared_sum = sum(y_squared)

    cc = (xy_sum - (x_sum * y_sum) / n) / (math.sqrt(x_squared_sum - (x_sum**2) / n) * math.sqrt(y_squared_sum - (y_sum**2) / n))
    return cc

if __name__ == '__main__':
    temp_celsius = [110, 110, 111, 111, 112, 112, 114, 114, 117, 117, 122, 122, 130, 130, 143, 143]
    stirring_rate_rpm = [30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]
    yield_percent = [70.27, 72.29, 72.57, 74.69, 76.09, 73.14, 75.61, 69.56, 74.41, 73.49, 79.18, 75.44, 81.71, 83.03, 76.98, 80.99]

    # a. Compute the correlation between temperature and yield. Interpret the result.
    result = correlation_coefficient(temp_celsius, yield_percent)
    print('Correlation between temperature and yield: ' + str(result))
    print('The given results shows a strong positive correlation between the two\n')

    # b. Compute the correlation between stirring rate and yield. Interpret the result.
    result = correlation_coefficient(stirring_rate_rpm, yield_percent)
    print('Correlation between stirring rate and yield: ' + str(result))
    print('The given results shows a strong positive correlation between the two\n')

    # c. Compute the correlation between temperature and stirring rate. Interpret the result
    result = correlation_coefficient(temp_celsius, stirring_rate_rpm)
    print('Correlation between temperature and stirring rate: ' + str(result))
    print('The given results shows a very strong positive correlation between the two, nearing 100%\n')