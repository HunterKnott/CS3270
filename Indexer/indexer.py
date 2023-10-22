'''Hunter Knott, CS 3270, Utah Valley University'''
import os

def main():
    # Specify the directory in the command line
    current_directory = os.getcwd()
    for item in os.scandir(current_directory):
        print(item)

if __name__ == '__main__':
    main()