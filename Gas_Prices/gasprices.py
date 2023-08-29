'''Examines weekly gas prices from 1994 to 2012'''

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

'''Read all file lines into a list'''
entries = []
with open('gas_prices.txt') as gas_file:
    for line in gas_file:
        entries.append(line.strip())

'''Make a list of the years included'''
years = []
for entry in entries:
    if entry[entry.index("-") + 4 :entry.index(":")] not in years:
        years.append(entry[entry.index("-") + 4 :entry.index(":")])

'''Separate entries into lists by year'''
entries_by_year = []
weekly_entries = []
for year in years:
    for entry in entries:
        if year in entry:
            weekly_entries.append(entry)
    entries_by_year.append(weekly_entries)
    weekly_entries = []

'''Separate year entries into lists by month'''
averages_by_month = []
month_sums = []
for year in entries_by_year:
    prices = []
    for entry in year:
        if len(prices) < int(entry[:entry.index("-")]):
            prices.append([])
        prices[len(prices) - 1].append(entry[entry.index(":") + 1:])
    prices = []

'''Simplify year entries to only the prices'''
for year in entries_by_year:
    for entry in year:
        entries_by_year[entries_by_year.index(year)][year.index(entry)] = entries_by_year[entries_by_year.index(year)][year.index(entry)][entry.index(":") + 1:]

'''Print out results'''
for year in years:
    print(year + ":")
    print("Low: $" + "___" + ", Avg: $" + "___" + ", High: $" + "___")
    # current_year = 0
    # years_passed = []
    # weekly_entries = []
    # averages = []
    # for line in gas_file:
    #     current_year = line[line.index("-") + 4 :line.index(":")]
    #     weekly_entries.append(float(line[line.index(":") + 1 :]))
    #     if len(averages) == int(line[:line.index("-")]) - 1:
    #         averages.append([])
    #     averages[int(line[:line.index("-")]) - 1].append(weekly_entries[len(weekly_entries) - 1])
    #     if not years_passed:
    #         years_passed.append(current_year)
    #         print(current_year)
    #     if current_year not in years_passed:
    #         print("Low: $" + "{:.2f}".format(min(weekly_entries)) + ", Avg: $" + "{:.2f}".format( sum(weekly_entries) / len(weekly_entries) ) + ", High: $" + "{:.2f}".format(max(weekly_entries)))
    #         for i in range(len(months)):
    #             # print(months[i] + " $" + "{:.2f}".format(sum(averages[i]) / len(averages[i])))
    #             print(months[i] + " $" + str(averages[i]))
    #         weekly_entries = []
    #         averages = []
    #         years_passed.append(current_year)
    #         print(current_year)
    # print("Low: $" + "{:.2f}".format(min(weekly_entries)) + ", Avg: $" + "{:.2f}".format( sum(weekly_entries) / len(weekly_entries) ) + ", High: $" + "{:.2f}".format(max(weekly_entries)))
    # print(months[i] + " $" + str(averages[i]))