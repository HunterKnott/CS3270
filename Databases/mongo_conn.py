# Hunter Knott, CS 3530, Utah Valley University
import sys
import pymongo

def main():
    # Connect to Mongodb
    client = pymongo.MongoClient("localhost",username='root',password="9WHeoU1KUcNG",authSource="admin")

    print ("pymongo version:", pymongo.version)

    # Set database
    my_db = client.contacts
    print("database:", my_db.name)

    # Read first 10 contacts
    for item in my_db.contacts.find().limit(10):
        print(item)

    if len(sys.argv) > 1:
        input = sys.argv[1]
    else:
        input = input("Enter a last name to search in the database: ")

    print("\nUser query results:")
    query = {"last_name": input}
    result_set = my_db.contacts.find(query)
    data_present = False

    for item in my_db.contacts.find(query):
        data_present = True
        print(item)

    if not data_present:
        print("There is no document with that last name")

if __name__ == "__main__":
    main()