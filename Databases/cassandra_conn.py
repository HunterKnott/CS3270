# Hunter Knott, CS 3530, Utah Valley University
import sys
from cassandra.cluster import Cluster

def main():
    # Connect to Cassandra cluster
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('contacts')

    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = input("Enter a last name to search in the database: ")
    
    print("\nUser query results:")
    result = session.execute(f"SELECT * FROM Contacts_by_names WHERE lastname = '{query}';")
    data_present = False

    for part in result:
        data_present = True
        print(part)
    
    if not data_present:
        print("There is no row with that last name")

    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()