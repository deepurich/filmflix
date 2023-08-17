from connect import * # import the connect.py module 


def delete(data):
    #use primary key (SongID) to delete a specific record.
    filmID = int(data['filmID'])

    # DELETE FROM songs table WHERE the SongID = idField(1/2/3/4/5.....)
    dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {filmID}")
    dbCnx.commit()

    
    print(f"Record {filmID}  deleted successfully, from tblFilms table. ")
if __name__=="__main__":
    delete()
