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
    # 0. Get names of all suppliers for projects in London
    london_projs = {j.jno for j in projects if j.city == 'London'} # Get list of all London jno's
    london_supp_ids = {r.sno for r in orders if r.jno in london_projs}
    london_supps = {s.sname for s in suppliers if s.sno in london_supp_ids}
    
    # 1. Get names of all suppliers that supply bolts.
    bolt_parts = {p.pno for p in parts if p.pname == 'Bolt'}
    bolt_supp_ids = {q.sno for q in orders if q.pno in bolt_parts}
    bolt_supps = {s.sname for s in suppliers if s.sno in bolt_supp_ids}
    print(bolt_supps)

    # 2. Get names of all suppliers that supply blue parts.
    blue_parts = {p.pno for p in parts if p.color == 'Blue'}
    blue_supp_ids = {q.sno for q in orders if q.pno in blue_parts}
    blue_supps = {s.sname for s in suppliers if s.sno in blue_supp_ids}
    print(blue_supps)

    # 3. Get names of all suppliers not used in Athens projects
    

    # 4. Get names and colors of all parts not used in Oslo
    # 5. Get pairs of names of all suppliers that are located in the same city.
    # 6. Print all suppliers out by city

if __name__ == '__main__':
    main()