'''Hunter Knott, CS 3270, Utah Valley University'''
import sqlite3

# Write a command-line Python program that creates an SQLite database with at least one table
def create_db(name):
    cx = sqlite3.connect(name)
    cursor = cx.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS menu_items (
            item_id INTEGER PRIMARY KEY,
            item_name VARCHAR(50),
            item_price DECIMAL(4, 2)
        );
    '''

    cursor.execute(create_table_query)
    cx.commit()
    cx.close()

# 1 Populate the database with sample data (at least 12 records)
def populate_db(name):
    cx = sqlite3.connect(name)
    cursor = cx.cursor()

    sample_data = [
        ('Caldo de Pollo', 12.99),
        ('Sopa a la Minuta', 18.99),
        ('Papa a la Huancaina', 10.99),
        ('Causa de Tuna', 13.99),
        ('Pollo a la Brasa Entera', 19.99),
        ('Aji de Gallina', 14.99),
        ('Arroz Chaufa', 16.99),
        ('Lomo Saltado', 18.99),
        ('Carapulcra', 14.99),
        ('Tallarin Saltado', 16.99),
        ('Inca Cola', 3.99),
        ('Chicha Morada', 3.99)
    ]

    insert_query = 'INSERT INTO menu_items (item_name, item_price) VALUES (?, ?);'
    cursor.executemany(insert_query, sample_data)

    cx.commit()
    cx.close

# 2 Clear the database (delete all records)
def clear_db(name):
    cx = sqlite3.connect(name)
    cursor = cx.cursor()

    delete_query = 'DELETE FROM menu_items;'
    cursor.execute(delete_query)

    cx.commit()
    cx.close()

# 3 Print all the items in the database
def print_items(name):
    cx = sqlite3.connect(name)
    cursor = cx.cursor()

    select_query = 'SELECT * FROM menu_items;'
    cursor.execute(select_query)

    items = cursor.fetchall()
    for item in items:
        print(item)

    cx.close()

# 4 Add an item
def add_item(name, item_name, item_price):
    cx = sqlite3.connect(name)
    cursor = cx.cursor()

    insert_query = 'INSERT INTO menu_items (item_name, item_price) VALUES (?, ?);'
    cursor.execute(insert_query, (item_name, item_price))

    cx.commit()
    cx.close()

# 5 Delete an item by ID
def delete_item(name, id):
    cx = sqlite3.connect(name)
    cursor = cx.cursor()

    delete_query = 'DELETE FROM menu_items WHERE item_id = ?;'
    cursor.execute(delete_query, (id,))

    cx.commit()
    cx.close()

# 6 Execute an SQL query that incorporates a user-selected value and print the results
def execute_query(name, query, params):
    cx = sqlite3.connect(name)
    cursor = cx.cursor()

    cursor.execute(query, params)
    results = cursor.fetchall()

    for result in results:
        print(result)

    cx.close()

if __name__ == '__main__':
    db_name = 'restaurant.db'
    create_db(db_name)

    while True:
        print('\nMenu:')
        print('1. Populate the database with sample data')
        print('2. Clear the database (delete all records)')
        print('3. Print all items in the database')
        print('4. Add an item')
        print('5. Delete an item by ID')
        print('6. Execute an SQL query with a user-selected value')
        print('7. Exit')

        choice = input('Enter your choice (1-7): ')

        if choice == '1':
            populate_db(db_name)
            print("Sample data added to database")
        elif choice == '2':
            clear_db(db_name)
            print("Database cleared")
        elif choice == '3':
            print_items(db_name)
        elif choice == '4':
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            add_item(db_name, item_name, item_price)
            print("Item added to database")
        elif choice == '5':
            item_id = int(input("Enter item ID to delete: "))
            delete_item(db_name, item_id)
            print("Item deleted from database")
        elif choice == '6':
            user_query = input("Enter SQL query: ")
            user_value = input("Enter user-selected value: ")
            execute_query(db_name, user_query, (user_value,))
        elif choice == '7':
            print("Exiting program")
            break
        else:
            print("Please enter a number between 1 and 7")