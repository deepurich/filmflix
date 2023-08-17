from connect import * # import the connect.py module 
import time # import the time to access date and time functions/method

# define a function called insert() 
def insert(data):    

    # Note: SongID is set to AUTOINCREMENT, therefore, input not required.
    filmID = int(data['filmID'])
    filmTitle = data['title']
    filmYR = int(data['yearReleased'])
    filmRating = data['rating']
    filmDuration = int(data['duration'])
    filmGenre = data['genre']
   
    # field names in songs table : SongID, Title, Artist and Genre
    # insert data captured from input function which is saved in their respective variables
    dbCursor.execute("INSERT INTO tblFilms (filmID,title,yearReleased,rating,duration,genre) VALUES (?,?,?,?,?,?)",(filmID,filmTitle,filmYR,filmRating,filmDuration,filmGenre)) # Use ? as placeholders
    dbCnx.commit() # Permanently write the change(s) to the table in the database

    # Delay execution for a given number of seconds.
    time.sleep(3)
    print(f"{filmTitle} inserted into the tblFilms table")

# if the main is the current file then call/invoke/execute the function insert(). Otherwise dont
if __name__ =="__main__":
    insert()

