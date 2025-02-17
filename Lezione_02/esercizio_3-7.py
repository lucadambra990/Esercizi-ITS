#Esercizio 3-7
invitated_p:list = ["Marek Hamsik", "Lorenzo Insigne", "Dries Mertens", "Edison Cavani", "Eziquiel Lavezzi"]
print("Il tavolo non arriverà in tempo per la cena, purtroppo posso invitare solo due persone...")
invitated_p.pop()
invitated_p.pop()
invitated_p.pop()
print("Voi siete ancora invitati " + invitated_p[0])
print("Voi siete ancora invitati " + invitated_p[1])
del invitated_p[0]
del invitated_p[0]
print(invitated_p) 