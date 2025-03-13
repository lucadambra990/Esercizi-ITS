def make_album(artist_name:str,album_title:str,numnber_of_songs:None):
    result ={"artist_name":artist_name, "album_title":album_title, "number_of_songs":number_of_songs}
    return result

while True:
    artist_name:str=input("Inserisci il nome dell'artista: ")
    if artist_name =="esci":
        break
    album_title:str=input("Inserisci il titolo dell'album: ")
    number_of_songs:int=int(input("Inserisci il numero delle canzoni dell'album: "))
    
    print(make_album(artist_name,album_title,number_of_songs))