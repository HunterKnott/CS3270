'''Examines weekly gas prices from 1994 to 2012'''

# f = open('gas_prices.txt', 'r')
# print(f.read())

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

with open('gas_prices.txt') as gas_file:
    current_year = 0
    years_passed = []
    weekly_prices = []
    for line in gas_file:
        current_year = line[line.index("-") + 4 :line.index(":")]
        weekly_prices.append(float(line[line.index(":") + 1 :]))
        if not years_passed:
            years_passed.append(current_year)
            print(current_year)
        if current_year not in years_passed:
            print("Low: $" + "{:.2f}".format(min(weekly_prices)) + ", Avg: $" + "{:.2f}".format( sum(weekly_prices) / len(weekly_prices) ) + ", High: $" + "{:.2f}".format(max(weekly_prices)))
            weekly_prices = []
            years_passed.append(current_year)
            print(current_year)
    print("Low: $" + "{:.2f}".format(min(weekly_prices)) + ", Avg: $" + "{:.2f}".format( sum(weekly_prices) / len(weekly_prices) ) + ", High: $" + "{:.2f}".format(max(weekly_prices)))