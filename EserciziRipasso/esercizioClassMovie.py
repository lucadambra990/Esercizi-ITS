class Movie:
    def __init__(self, movie_id:str,title:str,director:str,is_rented:bool=False):
        self.movie_id=movie_id
        self.title=title
        self.director=director
        self.is_rented=is_rented

    def rent(self):
        if self.is_rented is True:
            print(f"il Film '{self.title}' è già noleggiato")
        else:
            self.is_rented=True

    def return_movie(self):
        if self.is_rented is False:
            print(f"Il film {self.title} non è stato noleggiato da questo cliente")
        else:
            self.is_rented=False

class Customer:
    def __init__(self,customer_id:str,name:str):
        self.customer_id=customer_id
        self.name=name
        self.rented_movies=[]

    def rent_movie(self,movie:Movie):
        if movie.is_rented is False:
            self.rented_movies.append(movie)
            movie.rent()
            
        else:
            print(f"Il film '{movie.title}' è già noleggiato.")
        
    def return_movie(self,movie:Movie):
        if movie.is_rented is False:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")
        else:
            self.rented_movies.remove(movie)
            movie.return_movie()
            
            

class VideoRentalStore:
    
    def __init__(self):
        self.movies={}
        self.customers={}

    def add_movie(self,movie_id:str,title:str,director:str):
        if movie_id not in self.movies:
            new_movie = Movie(movie_id,title,director)
            self.movies[movie_id]=new_movie
        else:
            print(f"Il film con ID {movie_id} esiste già")
        
    def register_customer(self,customer_id:str,name:str):
        if customer_id not in self.customers:
            new_customer=Customer(customer_id,name)
            self.customers[customer_id]=new_customer
        else:
            print(f"Il cliente con ID {customer_id} è già registrato")
        
    def rent_movie(self,customer_id:str,movie_id:str):
        if customer_id not in self.customers or movie_id not in self.movies:
            print("Cliente o film non trovato.")
        else:  
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.rent_movie(movie)

    def return_movie(self,customer_id:str,movie_id:str):
        if customer_id not in self.customers or movie_id not in self.movies:
            print("Cliente o film non trovato.")
        else:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.return_movie(movie)

    def get_rented_movies(self,customer_id:str)->list[Movie]:
        if customer_id not in self.customers:
            print("Cliente non trovato.")
            return []
        else:
            return list(self.customers[customer_id].rented_movies)
