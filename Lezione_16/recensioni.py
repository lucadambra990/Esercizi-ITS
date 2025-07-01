class Media():
    _title:str
    _reviews:list[int]
    def __init__(self,title:str, reviews:list[int]):
        self._title = title
        self._reviews = [i for i in range(1,6)]

    def set_title(self, title:str):
        self._title = title

    def get_title(self) -> str:
        return self._title
    
    def aggiungiValutazione(self, voto:int):
        if voto in self._reviews:
            self._reviews.append(voto)
        else:
            raise ValueError("Voto non valido. Deve essere tra 1 e 5.")
        
    def getMedia(self) -> float:
        return sum(self._reviews) / len(self._reviews)
    
    def getRate(self)-> str:
        if len(self._reviews) == 0:
            return "Nessuna valutazione disponibile."
        media = self.getMedia()
        if media < 2:
            return "Terribile"
        elif media < 3:
            return "Brutto"
        elif media < 4:
            return "Normale"
        elif media < 5:
            return "Bello"
        else:
            return "Grandioso"
        
    def ratePercetage(self, voto:int) -> float:
        if voto not in self._reviews:
            raise ValueError("Voto non valido. Deve essere tra 1 e 5.")
        return (self._reviews.count(voto) / len(self._reviews)) * 100
    
    def recensione(self) -> str:
        return f"Titolo: {self._title}, Media: {self.getMedia()}, Terribile: {self.ratePercetage(1)}%, Brutto: {self.ratePercetage(2)}%, Normale: {self.ratePercetage(3)}%, Bello: {self.ratePercetage(4)}%, Grandioso: {self.ratePercetage(5)}%"