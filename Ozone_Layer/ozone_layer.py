'''Hunter Knott, CS 3270, Utah Valley University'''

import csv
from operator import itemgetter
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

# Puts all state/code pairs into a list
def read_state_codes():
    state_codes = {}
    with open("state_codes-1.txt", "r") as file:
        for line in file:
            code, state = line.strip().split(',')
            state_codes[code] = state

    return state_codes

# Puts all state/county pairs into a dictionary, used from provided counties_bu_state-1.py file
def read_state_counties():
    # Open CSV file
    f = open('daily_44201_2021.csv')
    rows = csv.reader(f)
    next(rows)                      # Ignore header line

    result = defaultdict(set)       # Store counties only once
    for fields in rows:
        state = fields[24]
        county = fields[25]
        result[state].add(county)   # County not duplicated in a set

    # Sort by state
    result = sorted(result.items(), key = itemgetter(0))
    states = []
    for state, counties in result:
        states.append(state)

    return result

# Displays SQI graph of specified state and county
# Based on user choice, graph will either be displayed on the screen or in a file
def draw_graph(state_name, county_name, data, output_file=None):
    selected_rows = data[(data['State Name'] == state_name) & (data['County Name'] == county_name)]
    aqi_list = selected_rows['AQI'].tolist()

    average_aqi = round(sum(aqi_list) / len(aqi_list))
    if average_aqi <= 50:
        line_color = 'green'
    else:
        line_color = 'red'

    plt.plot(aqi_list, label=f'{state_name}, {county_name}, Avg AQI: {average_aqi}', color=line_color, linewidth=0.5)
    plt.ylabel('AQI Values')
    plt.title('AQI Values for County')
    plt.title('AQI Values for ' + str(county_name) + ' County, ' + str(state_name) + ' (avg. AQI = ' + str(average_aqi) + ')')
    plt.legend()

    plt.axhline(y=average_aqi, color='black', linestyle='--', label='AQI Average (' + str(average_aqi) + ')')
    plt.xticks([])

    if output_file:
        plt.savefig(output_file)
        plt.close()
    else:
        plt.show()
        plt.close()

if __name__ == '__main__':
    print('Loading data...')
    counties = read_state_counties()
    state_codes = read_state_codes()
    epa_data = pd.read_csv('daily_44201_2021.csv', low_memory=False)

    # Continues to ask for 2-letter state codes until user quits
    while True:
        user_input = input("Enter 2-letter state code (Q to quit): ")
        state_code = user_input.upper()
        
        if state_code == 'Q':
            print("Quitting program")
            break

        if state_code in state_codes:
            # Continues to ask for a state county as long as user says yes
            while True:
                state_name = state_codes[state_code]
                state_tuple = [(state, counties) for state, counties in counties if state == state_name]
                result_counties = state_tuple[0] if state_tuple else None

                if result_counties:
                    i = 1
                    for county in sorted(result_counties[1]):
                        print(str(i) + ': ' + str(county))
                        i += 1
                    
                    user_input = input('Enter number for county: ')
                    county_name = sorted(result_counties[1])[int(user_input) - 1]
                else:
                    # This is the only 'state' without counties
                    # The DC string is case sensative and needs to be written like this
                    state_name = 'District Of Columbia'
                    county_name = 'District of Columbia'
                
                print('1 Screen')
                print('2 File')
                user_input = input('Choose destination for plot: ')

                # If user chooses to put a graph in a file, they will enter in a file name and extension
                if user_input == '2':
                    user_input = input('Enter file with extension of jpg|png|pdf: ')
                    valid_extensions = ['jpg', 'png', 'pdf']
                    if not any(user_input.lower().endswith(ext) for ext in valid_extensions):
                        print('Invalid file extension. Please enter a valid file extension.')
                    else:
                        # Create the file in the current directory
                        with open(user_input, 'w'):
                            draw_graph(str(state_name), str(county_name), epa_data, user_input)
                        print(f'File {user_input} created successfully in the current directory.')
                else:
                    # By default, the graph will be displayed on screen
                    draw_graph(str(state_name), str(county_name), epa_data)

                user_input = input('Another ' + str(state_name) + ' county? (y/n): ')
                if user_input == 'n':
                    break

        else:
            print("Invalid state code. Please enter a valid 2-letter state code.")