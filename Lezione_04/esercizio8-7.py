def make_album(artist_name:str, album_title:str, number_of_songs:int = None):
    if number_of_songs == None:
        return {"artist_name":artist_name, "album_title":album_title}
    else:
        return {"artist_name":artist_name, "album_title":album_title, "number_of_songs":number_of_songs}
    
print(make_album("Salmo", "Flop"))
print(make_album("Lazza", "Locura",19))
print(make_album("Geolier", "Dio lo sa",21))