'''Hunter Knott, CS 3270, Utah Valley University'''
from collections import namedtuple

parts = set()
# Part = namedtuple('pno', ['pname', 'color', 'weight', 'city'])
with open('parts.txt') as parts_file:
    lines = [line.strip() for line in parts_file.readlines()]
headers = lines[1].split(',')
print(headers)
Part = namedtuple(headers[0], [headers[1], headers[2], headers[3]])
for line in lines[2:]:
    entry = line.split(',')
    parts.add(Part(entry[0], [entry[1], entry[2], entry[3]]))

projects = set()

suppliers = set()

entries = set()

def main():
    pass

if __name__ == '__main__':
    main()