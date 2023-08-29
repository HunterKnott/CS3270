'''Examines weekly gas prices from 1994 to 2012'''

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
for year in entries_by_year:
    prices = []
    for entry in year:
        if len(prices) < int(entry[:entry.index("-")]):
            prices.append([])
        prices[len(prices) - 1].append(float(entry[entry.index(":") + 1:]))
    averages_by_month.append(prices)
    prices = []

'''Simplify year entries to only the prices'''
for year in entries_by_year:
    for entry in year:
        entries_by_year[entries_by_year.index(year)][year.index(entry)] = float(entries_by_year[entries_by_year.index(year)][year.index(entry)][entry.index(":") + 1:])

'''Print out results'''
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for year in years:
    print(year + ":")
    print("    Low: $" + "{:.2f}".format(float(min(entries_by_year[years.index(year)]))) + ", Avg: $" + "{:.2f}".format( sum(entries_by_year[years.index(year)]) / len(entries_by_year[years.index(year)])) + ", High: $" + "{:.2f}".format(float(max(entries_by_year[years.index(year)]))))
    for month in months:
        print("    " + month + ":" + " " * (10 - len(month)) + "{:.2f}".format(sum(averages_by_month[years.index(year)][months.index(month)]) / len(averages_by_month[years.index(year)][months.index(month)] )))
    print("\n")