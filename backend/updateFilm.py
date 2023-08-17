from connect import *
import time
def update(data):
   
    #use primary key (SongID) to update a specific record.
    filmID = int(data['filmID'])
    filmTitle = data['title']
    filmYR = int(data['yearReleased'])
    filmRating = data['rating']
    filmDuration = int(data['duration'])
    filmGenre = data['genre']

    # UPDATE songs SET {Title or Artist or Genre} = "TitleValue/ArtistValue/GenreValue" WHERE SongID = 1/2/3/4...
    print(f"UPDATE tblFilms SET title='{filmTitle}',yearReleased={filmYR},rating='{filmRating}',duration={filmDuration},genre='{filmGenre}' WHERE filmID = {filmID}")
    dbCursor.execute(f"UPDATE tblFilms SET title='{filmTitle}',yearReleased={filmYR},rating='{filmRating}',duration={filmDuration},genre='{filmGenre}' WHERE filmID = {filmID}")
    dbCnx.commit()
    print(f"Record {filmID}  updated successfully, in tblFlims table. ")
   
if __name__=="__main__":
    update()