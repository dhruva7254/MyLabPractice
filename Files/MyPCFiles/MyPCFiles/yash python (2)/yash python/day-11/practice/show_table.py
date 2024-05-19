import mysql.connector
cnx=mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
cur.execute("select * from student where marks<30")
for row in cur:
    print(row)
cnx.commit()
cnx.close()