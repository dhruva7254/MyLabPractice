import mysql.connector
cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
cur.execute("""CREATE TABLE student2( 
            roll_no INT, 
            subid varchar(10), 
            marks INT);""")
cnx.commit()
cnx.close()
