from connect import * # import the connect.py module
 
# define a function called reports()
def reports():
    # dbCursor.execute("SELECT * FROM songs ORDER BY Genre DESC")
    # dbCursor.execute("SELECT * FROM songs ORDER BY Genre ASC")
    # dbCursor.execute("SELECT * FROM songs ORDER BY Artist ASC")
    # dbCursor.execute("SELECT Artist, Title FROM songs")
    # dbCursor.execute("SELECT * FROM songs WHERE Genre = 'Soul' or Genre = 'Pop' ")
    # dbCursor.execute("SELECT * FROM songs WHERE Title LIKE 'd%' ")
    # dbCursor.execute("SELECT * FROM songs WHERE Title NOT LIKE 'd%' ")
    dbCursor.execute("SELECT * FROM tblFilms WHERE Title LIKE '%d%' ")
 
    #fetch all selected records using the fetchall() method and save it in the allRecords variable
    allRecords = dbCursor.fetchall()
 
    #loop through the allRecords variable
    for eachRecord in allRecords:
 
        #print eachRecord in the list of allRecords variable
        print(eachRecord)
 
if __name__=="__main__":
    reports()
 
