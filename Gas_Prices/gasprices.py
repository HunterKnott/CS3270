'''Examines weekly gas prices from 1994 to 2012'''

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

with open('gas_prices.txt') as gas_file:
    current_year = 0
    years_passed = []
    weekly_prices = []
    averages = []
    for line in gas_file:
        current_year = line[line.index("-") + 4 :line.index(":")]
        weekly_prices.append(float(line[line.index(":") + 1 :]))
        if len(averages) == int(line[:line.index("-")]) - 1:
            averages.append([])
        averages[int(line[:line.index("-")]) - 1].append(weekly_prices[len(weekly_prices) - 1])
        if not years_passed:
            years_passed.append(current_year)
            print(current_year)
        if current_year not in years_passed:
            print("Low: $" + "{:.2f}".format(min(weekly_prices)) + ", Avg: $" + "{:.2f}".format( sum(weekly_prices) / len(weekly_prices) ) + ", High: $" + "{:.2f}".format(max(weekly_prices)))
            for i in range(len(months)):
                # print(months[i] + " $" + "{:.2f}".format(sum(averages[i]) / len(averages[i])))
                print(months[i] + " $" + str(averages[i]))
            weekly_prices = []
            averages = []
            years_passed.append(current_year)
            print(current_year)
    print("Low: $" + "{:.2f}".format(min(weekly_prices)) + ", Avg: $" + "{:.2f}".format( sum(weekly_prices) / len(weekly_prices) ) + ", High: $" + "{:.2f}".format(max(weekly_prices)))