import mysql.connector

# // -- > comment < -- // 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = 'root',
    database = 'prueba'
)

cursor = mydb.cursor()

# // -- > data list < -- //0
cursor.execute("SELECT * FROM usuario")
result = cursor.fetchall()
print(result)

# // -- > view structure in table < -- //
# cursor.execute('SHOW CREATE TABLE usuario')
# result = cursor.fetchall()
# print((result))

# // -- > insert data < -- // 
# sql = 'insert into usuario (full_name, email, birth_day) values (%s, %s, %s)'
# values = ('Lola la Trailera','dosMujeres@unCamino.com', '69')
# cursor.execute(sql, values)
# mydb.commit()
# print(cursor.rowcount)

# // -- > update data < -- // 
# sql = 'UPDATE usuario SET email = %s where id = %s'
# values = ('micorreo@correo.com', 4)
# cursor.execute(sql, values)
# mydb.commit()
# print(cursor.rowcount)

# // -- > delete data < -- // 
# sql = 'DELETE FROM usuario WHERE id = %s'
# values = (4, )
# cursor.execute(sql, values)
# mydb.commit()
# print(cursor.rowcount)






#result = cursor.fetchone()

# print(result)
# 
# if __name__ == "__main__":
#     print ("Executed when invoked directly")
# else:
#     print ("Executed when imported")

# print(__name__)