import mysql.connector
cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur=cnx.cursor()
#cur.execute("""CREATE TABLE mobiledetails(name varchar(20),mobileno varchar(20));""")
#record=[["yash","9834087342"],["bholanath","9652325650"],["pranjal","9825642351"],["janvi","9333033012"],["jack","9352235683"],
#        ["harish","9332633521"],["tomy","9933556622"],["utkarsh","9832654525"],["trim","9865457833"],["hgrt","7218621361"]]
#for name,mobileno in record:
#    querry="insert into mobiledetails values("+\
#                repr(name)+","+\
#                repr(mobileno)+");"
#    print(querry)
#    cur.execute(querry)
#cur.execute("select * from mobiledetails")
#cur.execute("select * from mobiledetails where mobileno regexp '^98.';" )
cur.execute("select * from mobiledetails where mobileno regexp '3.*3.*3.*';")
for row in cur:
    print(row)
cnx.commit()
cnx.close()
