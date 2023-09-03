'''Hunter Knott, CS 3270, Utah Valley University'''
from collections import namedtuple

parts = set()
with open('parts.txt') as parts_file:
    lines = [line.strip() for line in parts_file.readlines()]
headers = lines[1].split(',')
Part = namedtuple('Part', [headers[0], headers[1], headers[2], headers[3], headers[4]])
for line in lines[2:]:
    entry = line.split(',')
    parts.add(Part(entry[0], entry[1], entry[2], entry[3], entry[4]))

projects = set()
with open('projects.txt') as projects_file:
    lines = [line.strip() for line in projects_file.readlines()]
headers = lines[1].split(',')
Project = namedtuple('Project', [headers[0], headers[1], headers[2]])
for line in lines[2:]:
    entry = line.split(',')
    projects.add(Project(entry[0], entry[1], entry[2]))

suppliers = set()
with open('suppliers.txt') as suppliers_file:
    lines = [line.strip() for line in suppliers_file.readlines()]
headers = lines[1].split(',')
Supplier = namedtuple('Supplier', [headers[0], headers[1], headers[2], headers[3]])
for line in lines[2:]:
    entry = line.split(',')
    suppliers.add(Supplier(entry[0], entry[1], entry[2], entry[3]))

orders = set()
with open('spj.txt') as spj_file:
    lines = [line.strip() for line in spj_file.readlines()]
headers = lines[1].split(',')
Order = namedtuple('Order', [headers[0], headers[1], headers[2], headers[3]])
for line in lines[2:]:
    entry = line.split(',')
    orders.add(Order(entry[0], entry[1], entry[2], entry[3]))

def main():
    pass

if __name__ == '__main__':
    main()