import mysql.connector
records=[[1,'sub1',34],
         [2,'sub1',30],
         [3,'sub1',23],
         [1,'sub2',23],
        [2,'sub2',26],
        [3,'sub2',30],
        [1,'sub3',30],
        [2,'sub3',30],
        [3,'sub3',27],
    ]
cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
for rno, sub, marks in records:
    query = "insert into student values(" +\
                str(rno)+","+\
                repr(sub) + ","+\
                str(marks)+");"
    print(query)
    cur.execute(query)

cnx.commit()
cnx.close()
