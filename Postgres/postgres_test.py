# Hunter Knott, CS 3530, Utah Valley University
import psycopg2 # sqlalchemy is another way to do this
import sys
import csv
import json

def initial_query(cursor):
    postgreSQL_select_Query = "select stuID,lastName,firstName,majorid,credits from Students limit 10"
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from student table using cursor.fetchall")
    student_records = cursor.fetchall()
    print("Print each row and it's columns values")
    for row in student_records:
        print("stuId = ", row[0], )
        print("lastName = ", row[1])
        print("firstName = ", row[2])
        print("major = ", row[3])
        print("credits  = ", row[4], "\n")

def id_query(cursor, value):
    pg_select_by_id = f"""
    SELECT s.stuID, s.lastName, s.firstName, m.majorDesc, s.credits
    FROM Students s
    Join Majors m ON s.majorID = m.majorID
    WHERE stuId = {value}"""
    cursor.execute(pg_select_by_id)
    student_record = cursor.fetchone()
    
    if student_record:
        csv_helper(student_record)
        json_helper(student_record)
    else:
        print("No records found for the given ID.")

def lastname_query(cursor, value):
    pg_select_by_lastname = f"""
    SELECT s.stuID, s.lastName, s.firstName, m.majorDesc, s.credits
    FROM Students s
    JOIN Majors m ON s.majorID = m.majorID
    WHERE lastName = '{value}'"""
    cursor.execute(pg_select_by_lastname)
    student_records = cursor.fetchall()

    if student_records:
        csv_helper(student_records)
        json_helper(student_records)
    else:
        print("No records found for the given last name.")

def major_query(cursor, value):
    if value not in ['1', '2', '3', '4']:
        print('Input invalid. Possible input values: 1, 2, 3, 4')
        return

    pg_select_by_major = f"""
        SELECT s.stuID, s.lastName, s.firstName, m.majorDesc, s.credits
        FROM Students s
        JOIN Majors m ON s.majorID = m.majorID
        WHERE s.majorId = {value}"""
    cursor.execute(pg_select_by_major)
    student_records = cursor.fetchall()
    
    if student_records:
        csv_helper(student_records)
        json_helper(student_records)
    else:
        print("No records found for the given major.")

def rank_query(cursor, value):
    if value.lower() == 'freshman':
        query = 'BETWEEN 0 AND 29'
    elif value.lower() == 'sophomore':
        query = 'BETWEEN 30 AND 59'
    elif value.lower() == 'junior':
        query = 'BETWEEN 60 AND 89'
    elif value.lower() == 'Senior':
        query = '> 90'
    else:
        print('Input invalid. Possible input values: Freshman, Sophomore, Junior, Senior')
        return

    pg_select_by_rank = f"""
        SELECT s.stuID, s.lastName, s.firstName, m.majorDesc, s.credits
        FROM Students s
        JOIN Majors m ON s.majorID = m.majorID
        WHERE s.credits {query}"""
    cursor.execute(pg_select_by_rank)
    student_records = cursor.fetchall()

    if student_records:
        csv_helper(student_records)
        json_helper(student_records)
    else:
        print("No records found for the given rank.")
    
    # Freshman: 0-29 credits
    # Sophomore: 30-59
    # Junior: 60-89
    # Senior: 90+

def csv_helper(record):
    with open('data.csv', 'w', newline='') as csvfile:
        data_writer = csv.writer(csvfile, delimiter='~')
        data_writer.writerow(['stuID', 'lastName', 'firstName', 'major', 'credits'])
        
        if isinstance(record, list):
            for row in record:
                data_writer.writerow(row)
        elif record is not None:
            data_writer.writerow(record)

def json_helper(record):
    data = []

    if isinstance(record, list):
        for record in record:
            data.append({
                'stuID': record[0],
                'lastName': record[1],
                'firstName': record[2],
                'major': record[3],
                'credits': record[4]
            })
    elif record is not None:
        data.append({
            'stuID': record[0],
            'lastName': record[1],
            'firstName': record[2],
            'major': record[3],
            'credits': record[4]
        })

    with open('data.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

def main():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="UVUCS3520D4t4Th30ry!",
                                    host="127.0.0.1",
                                    port=5432,
                                    database="university")
        
        # Docker must be running for this to work
        cursor = connection.cursor()

        if len(sys.argv) == 3:
            query_type = sys.argv[1].lower()
            query_value = sys.argv[2]

            if query_type == 'id':
                id_query(cursor, query_value) # Ex. 100001
            elif query_type == 'lastname':
                lastname_query(cursor, query_value) # Ex. Veloz
            elif query_type == 'major':
                major_query(cursor, query_value) # Ex. 4
            elif query_type == 'rank':
                rank_query(cursor, query_value) # Ex. Junior
            elif query_type == 'initial':
                initial_query(cursor) # Doesn't use second parameter
            else:
                print('Input invalid. Possible input values: Id, Lastname, Major, Rank, Initial')
        
        elif len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1].lower() == 'initial'):
            initial_query(cursor)
        else:
            print('Command line input invalid. Must provide both a query type and search value, nothing else')
            print('Possible query types: Id, Lastname, Major, Rank, Initial')
        


    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)

    finally:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

if __name__ == "__main__":
    main()