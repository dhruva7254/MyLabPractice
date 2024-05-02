
import mysql.connector
# # Create new table
# cnx = mysql.connector.connect(user='root', 
#                               password='root123',
#                               host='127.0.0.1',
#                               database='mytrial')
# cur = cnx.cursor()
# cur.execute("""CREATE TABLE mobiledetails( 
#             name varchar(20),  
#             mobileno varchar(20));""")
# cnx.commit()
# cnx.close()
# # Insert records
# records=[['qwe','3456127890'],
#          ['wer','9812345670'],
#          ['ert','2300013456'],
#          ['rty','9876980002'],
#          ['tyu','2678564329'],
#          ['yui','9887654321'],
#          ['uio','3000765438'],
#          ['iop','3098765422'],
#          ['opa','9865432994'],
#          ['pas','2700076543'],
#     ]

# cnx = mysql.connector.connect(user='root', 
#                               password='root123',
#                               host='127.0.0.1',
#                               database='mytrial')
# cur = cnx.cursor()
# for name, mobileno in records:
#     query = "insert into mobiledetails values(" +\
#                 repr(name) + ","+\
#                 repr(mobileno)+");"
#     print(query)
#     cur.execute(query)
# cnx.commit()
# cnx.close()
# Select records and display them
cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
# cur.execute("select * from mobiledetails")
# cur.execute("select name,mobileno from mobiledetails where mobileno like "98%" ")
# cur.execute("select * from mobiledetails where mobileno like "%000%" ")
cur.execute("select name,mobileno from mobiledetails where mobileno regexp '^98' ")

for row in cur:
    print(row)
cnx.close()
