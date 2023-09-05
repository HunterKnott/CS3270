'''Hunter Knott, CS 3270, Utah Valley University'''
from collections import namedtuple

def read_file(file_name):
    data = set()
    with open(file_name) as data_file:
        lines = [line.strip() for line in data_file.readlines()]
    headers = lines[1].split(',')
    Instance = namedtuple(lines[0], [*headers])
    for line in lines[2:]:
        entry = line.split(',')
        data.add(Instance(*entry))
    return data

def main():
    parts = read_file('parts.txt')
    projects = read_file('projects.txt')
    suppliers = read_file('suppliers.txt')
    orders = read_file('spj.txt')

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
    athens_projs = {j.jno for j in projects if j.city == 'Athens'}
    athens_supp_ids = {r.sno for r in orders if r.jno in athens_projs}
    athens_supps = {s.sname for s in suppliers if s.sno in athens_supp_ids}
    non_athens_supps = {s.sname for s in suppliers if s.sname not in athens_supps}
    print(non_athens_supps)

    # 4. Get names and colors of all parts not used in Oslo
    oslo_projects = {j.jno for j in projects if j.city == 'Oslo'}
    oslo_supp_ids = {p.pno for p in orders if p.jno in oslo_projects}
    oslo_part_entries = {tuple([p.pname, p.color]) for p in parts if p.pno in oslo_supp_ids}
    non_oslo_part_entries = {tuple([p.pname, p.color]) for p in parts if tuple([p.pname, p.color]) not in oslo_part_entries}
    print(non_oslo_part_entries)

    # 5. Get pairs of names of all suppliers that are located in the same city.
    supplier_pairs = {(s1.sname, s2.sname)
        for s1 in suppliers for s2 in suppliers
        if s1.city == s2.city and s1.sname < s2.sname}
    print(supplier_pairs)

    # 6. Print all suppliers out by city
    city_suppliers = {s.city: {r.sname for r in suppliers
        if tuple([r.city, s.sname]) == tuple([s.city, s.sname])} for s in suppliers}
    print(city_suppliers)

if __name__ == '__main__':
    main()