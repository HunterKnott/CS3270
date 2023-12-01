# Run the following before use: pip install mysql-connector-python
import mysql.connector
from datetime import datetime

def mysql_connect():
    return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="AdminPassword",
        database="lab13_db"
    )

def write_data(conn, employee_id, firstname, lastname, phone_number):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Customer (employee_id, firstname, lastname, phone_number)
        VALUES (%s, %s, %s, %s)
        """, (employee_id, firstname, lastname, phone_number))
    
    conn.commit()
    cursor.close()

def update_customer_phone(conn, employee_id, new_phone_number):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Customer
        SET phone_number = %s
        WHERE employee_id = %s
    """, (new_phone_number, employee_id))

    conn.commit()
    cursor.close()

def make_trigger(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER phone_trigger
        AFTER UPDATE ON Customer
        FOR EACH ROW
        BEGIN
            INSERT INTO Customer_Audit (employee_id, change_on)
            VALUES (NEW.employee_id, NOW());
        END
    """)
    conn.commit()
    cursor.close()

def delete_data(conn, employee_id):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Customer
        WHERE employee_id = %s
        """, (employee_id,))
    
    conn.commit()
    cursor.close()

def display_user(conn):
    cursor = conn.cursor()
    cursor.execute("SET GLOBAL log_bin_trust_function_creators = 1")
    cursor.execute("SELECT CURRENT_USER()")
    current_user_result = cursor.fetchone()
    if current_user_result:
        current_user = current_user_result[0]
        print(f"\nCurrent User: {current_user}")
    
    conn.commit()
    cursor.close()

def read_all_data(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.*, MAX(ca.change_on) AS last_update_date
        FROM Customer c
        LEFT JOIN Customer_Audit ca ON c.employee_id = ca.employee_id
        GROUP BY c.employee_id
    """)

    customers = cursor.fetchall()
    for customer in customers:
        print(f"Employee ID: {customer[0]}, Name: {customer[1]} {customer[2]}, Phone: {customer[3]}, Last Update: {customer[4]}")

    cursor.close()

if __name__ == "__main__":
    connection = mysql_connect()

    # Set up phone number trigger
    make_trigger(connection)

    # Sample data
    for i in range(1, 11):
        write_data(connection, i, f"Customer{i}", f"LastName{i}", f"123-456-78{i}")

    # Initial data display
    display_user(connection)
    print("\nDisplaying all customers:")
    read_all_data(connection)

    # Update 2 customer phone numbers to activate trigger
    update_customer_phone(connection, 3, "999-999-9999")
    update_customer_phone(connection, 8, "111-111-1111")

    # Delete a customer
    delete_data(connection, 7)

    # Display all customers after changes
    display_user(connection)
    print("\nDisplaying all customers after changes:")
    read_all_data(connection)

    connection.close()