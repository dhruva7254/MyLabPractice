
import mysql.connector
# Create new table
cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
cur.execute("""CREATE TABLE mobiledetails( 
            name varchar(20),  
            mobileno varchar(20));""")
cnx.commit()
cnx.close()

# Insert records
records=[['qwe','3456127890'],
         ['wer','9812345670'],
         ['ert','2300013456'],
         ['rty','9876980002'],
         ['tyu','2678564329'],
         ['yui','9887654321'],
         ['uio','3000765438'],
         ['iop','3098765422'],
         ['opa','9865432994'],
         ['pas','2700076543'],
    ]

cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
for name, mobileno in records:
    query = "insert into mobiledetails values(" +\
                repr(name) + ","+\
                repr(mobileno)+");"
    print(query)
    cur.execute(query)

cnx.commit()
cnx.close()

# Select records and display them
cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
cur.execute("select * from mobiledetails")

# cur.execute("select name,mobileno from mobiledetails where mobileno like "98%"")
# cur.execute("select * from mobiledetails where mobileno like "%000%"")

for row in cur:
    print(row)


cnx.close()


"""Another syntax"""
# from mysql.connector import connect
""" Connect to mySQL server and create new data base"""
"""
with connect(host="localhost",user="root",password="root123") as connection:
    #        print(connection)
    #query="CREATE DATABASE mytrial;"
    #with connection.cursor() as cur:
    #    cur.execute(query)
    print("Successfully created a new database")
    query="SHOW DATABASES"
    with connection.cursor() as cur:
        cur.execute(query)
        for db in cur:
            print(db)
"""

""" Connecting to existing database and creating a table """
"""
with connect(host="localhost",user="root",
	password="root123", 
	database="mytrial") as connection:
    #print(connection)
    # Create Table
    query = "CREATE TABLE student( roll_no INT PRIMARY KEY, name varchar(10));"
    with connection.cursor() as cur:
        cur.execute(query)
    print("Successfully Created a table name student")
"""
""" Connect to Existing Database and insert records in existing table """
"""
with connect(host="localhost",user="root",password="root123", database="mytrial") as connection:
    #print(connection)
    # Insert multiple records in a table
    query = "INSERT INTO student (roll_no,name) VALUES ( %s, %s );"
    student_records=[(1,"xyz"),(2,"pqr"),(3,"abhi")]
    with connection.cursor() as cur:
        cur.executemany(query,student_records)
        connection.commit()
    print("Successfully Inserted multiple student records")
"""
""" Connect to Existing Database and select records from existing table """
"""
with connect(host="localhost",user="root",password="root123", database="mytrial") as connection:
    #print(connection)
    # Select records and print them
    query = "select * from student;"
    with connection.cursor() as cur:
        cur.execute(query)
        for row in cur:
            print(row)
""" 



