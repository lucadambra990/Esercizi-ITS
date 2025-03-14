from typing import Any

# class Admin:
#     def __init__(self):
#         pass


class Persona:
    def __init__(self,nome,cognome,eta):
        self.nome=nome #per inizializzare un attributo privato la sintassi è __nome, più in là si vedrà come farlo con i decorators
        self.cognome=cognome
        self.eta=eta
        self.password="password"
    def get_nome(self): #funzione getter, serve a restituire il valore della funzione(in questo esempio nome)
        return self.nome
    
    def set_name(self, nome):#funzione setter serve a modificare il valore della funzione presi dagli attributi della classe principale(in questo esempio nome).Setter ci aiuta ancha a modificare valori privati all'inteno di una classe
        self.nome=nome

    def get_password(self, tipo:Any):
        # if type(tipo) == Admin:
            return self.password
        # raise ValueError("Non puoi accedere alla password") #se il tipo di input non è Admin, non è possibile accedere alla password
    
    def set_password(self, password):
        self.password=password
        # raise ValueError("Non puoi modifcare la password") #in caso di attributo password privato

class Dipendente(Persona):
    def __init__(self, nome, cognome, eta, stipendio):

        super().__init__(nome, cognome, eta)
        self.stipendio=stipendio

    def get_stipendio(self):
        return self.stipendio
    
    def set_stipendio(self, stipendio):
        self.stipendio=stipendio


persona1:Persona=Persona("Luca","D'Ambra",21)
persona2:Persona=Persona("Flavio","Giorgi",30)
persona3:Persona=Persona("Fabrizio","Corona",42)
persona4:Persona=Persona("Fabrizio","Corona",42)