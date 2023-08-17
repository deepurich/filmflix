import sqlite3 as sql # import the sqlite3 module

# print(dir(sql))

# To use the sqlite3 module, start ny creating a database connection object(variable)
dbCnx = sql.connect("filmflix.db", check_same_thread=False)# create db or open db(if exists)

# #Create a cursor(variable) 
dbCursor = dbCnx.cursor()
