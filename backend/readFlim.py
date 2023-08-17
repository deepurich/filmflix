from connect import * # import the connect.py module 
import json
# define a function called read() 
def read():
    # select all records in the songs table
    dbCursor.execute("SELECT * FROM tblFilms")

    #fetch all selected records using the fetchall() method and save it in the allRecords variable
    allRecords = dbCursor.fetchall()
    filmsDict = []
    for film in allRecords:
        print(film)
        filmDict = {
            'filmID': film[0],
            'title': film[1],
            'yearReleased': film[2],
            'rating': film[3],
            'duration': film[4],
            'genre': film[5]
        }
        filmsDict.append(filmDict)
    return filmsDict

if __name__=="__main__":
    read()
  