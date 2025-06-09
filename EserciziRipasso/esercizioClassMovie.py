class Movie:
    def __init__(self, movie_id:str,title:str,director:str,is_rented:bool):
        self.movie_if=movie_id
        self.title=title
        self.director=director
        self.is_rented=is_rented

    def rent(self):
        if self.is_rented is True:
            raise Exception(f"il Film {self.title} è già noleggiato")
        else:
            self.is_rented==True

    def return_movie(self):
        if self.is_rented is False:
            raise Exception(f"Il film {self.title} non è stato noleggiato da questo cliente")
        else:
            self.is_rented==False

class Customer:
    def __init__(self,customer_id:str,name:str,rented_movies:list[Movie]=[]):
        self.customer_id=customer_id
        self.name=name
        self.rented_movies=rented_movies

    def rent_movie(self,movie:Movie):
        if movie.is_rented is False:
            self.rented_movies.append(movie)
        else:
            raise Exception(f"Il film {movie.title} è già noleggiato")
        
    def return_movie(self,movie:Movie):
        if movie.is_rented is False:
            raise Exception(f"Il film {movie.title} non è stato noleggiato da questo cliente")
        else:
            self.rented_movies.remove(movie)

class VideoRentalStore:
    
    def __init__(self, movies:dict[str,Movie],customers:dict[str,Customer]):
        self.movies=movies
        self.customers=customers

    def add_movie(self,movie_id:str,title:str,director:str):
        if movie_id not in self.movies:
            new_movie = Movie(movie_id,title,director)
            self.movies[movie_id]=new_movie
        else:
            raise Exception(f"Il film con ID {movie_id} esiste già")
        
    def register_customer(self,customer_id:str,name:str):
        if customer_id not in self.customers:
            new_customer=Customer(customer_id,name)
            self.customers[customer_id]=new_customer
        else:
            raise Exception(f"Il cliente con ID {customer_id} è già registrato")
        
    def rent_movie(self,customer_id:str,movie_id:str):
        if customer_id not in self.customers or movie_id not in self.movies:
            raise Exception("Cliente o film non trovato")
        else:  
            self.customers[customer_id].rent_movie(self.movies[movie_id])

    def return_movie(self,customer_id:str,movie_id:str):
        if customer_id not in self.customers or movie_id not in self.movies:
            raise Exception("Cliente o film non trovato")
        else:
            self.customers[customer_id].return_movie(self.movies[movie_id])

    def get_rented_movies(self,customer_id:str)->list[Movie]:
        if customer_id not in self.customers:
            raise Exception("Cliente non trovato")
        else:
            return list(Customer.rented_movies)
        
    # def get all movies 
        # lista di tutti i film che sono stati noleggiati da tutti i clienti

    def get_all_movies(self)->list[Movie,Customer]:
        lista_filmClient:list=[]
        for key, value in self.customers:
            for key, value in self.movies:
                lista_filmClient.append(self.customers[value],self.movies[value])
        return lista_filmClient