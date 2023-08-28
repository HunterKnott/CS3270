'''Examines weekly gas prices from 1994 to 2012'''

# f = open('gas_prices.txt', 'r')
# print(f.read())

with open('gas_prices.txt') as gas_file:
    current_year = 0
    new_year = 0
    for line in gas_file:
        new_year = line[line.index("-") + 4 :line.index(":")]
        if current_year != new_year:
            current_year = new_year
            print(current_year + ":")