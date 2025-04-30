class MovieCatalog:
    '''
    
    Attributi della classe Movie Catalog
    self.catalog:dict[str,list[str]]

    '''

    # inizializzare un oggetto della classe MovieCatalog
    def __init__(self)->None:
        self.setCatalog()

    #metodo str per visualizzare un catalogo
    def __str__(self):
        pass



    # metodi setter

    # metodo che imposta il valore dell'attributo setCatalog()
    def setCatalog(self)->None: # per ogni metodo di classe bisogna dare come argomento la keyword self per far capire a python che il metodo creato sia un metodo della classe
        self.catalog:dict[str,list[str]] = {}

    # metodo getter

    # metodo che ritorna il valore dell'attributo setCatalog()
    def getCatalog(self)->dict[str,list[str]]:
        return self.catalog
    
    # metodi della classe MovieCatalog

    # metodo che aggiunge una lista di film al catalogo
    def add_movie(self,director_name:str,movies:list[str])->None:
        # check valore valido di director_name
        if not director_name:
            print("Fornire un nome valido per il regista")
        #check valore valido di movies
        elif not movies:
            print("Fornire una lista di film che non sia vuota")
        # se poi i dati inseriti sono validi
        else:
            # se il registra è presente nel catalogo, aggiungi i film
            if director_name in self.catalog:
                # aggiungere film al catalogo
                for movie in movies:
                    # controlliamo se i film della lista movies siano già stati inseriti dentro al catalogo
                    # dizionario[key] -> ritorna il valore corrispondente alla chiave key
                    # self.catalog[director_name] è la lista dei film prodotti dal registra director_name
                    # dove self.catalog è un dizionario
                    # self.catalog[director_name] è il valorea corrispondente alla chiave director_name
                    if movie in self.catalog[director_name]: 
                        print(f"Il film {movie} è gia presente nel catalogo")
                    # un film della lista non è già presente nel catalogo    
                    else:
                        # aggiungere il film al catalogo
                        self.catalog[director_name].append(movie)
            # se il registra non è presente nel catalogo, creare un nuovo record
            # che ha come chiave il nome del regista e come valore la lista di film movies
            else:
                self.catalog[director_name] = movies


    # metodo che rimuove un film dal catalogo
    def remove_movie(self,director_name:str,movie:str)->None:
        if not director_name:
            print("Fornire un nome valido per il regista")
        #check valore valido di movie
        elif not movie:
            print("Fornire una film valido")
        # se poi i dati inseriti sono validi
        else:
            # se il registra è presente nel catalogo, rimuovi il film
            # e check se il film da rimuovere è presente nella lista dei film prodotti dal regista
            if director_name in self.catalog and movie in self.catalog[director_name]:

                #rimuovere il film dalla lista
                self.catalog[director_name].remove(movie)

            # se la lista di film è vuota rimuovi il regista dal cataologo
            if not self.catalog[director_name]:
                # rimuovi il registra dal catalogo
                del self.catalog[director_name]
    def list_directors(self)->list[str]:
        return list(self.catalog.keys())
