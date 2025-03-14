#Esercizio 3-6
invitated_p:list[str] = ["Marek Hamsik", "Lorenzo Insigne", "Dries Mertens", "Edison Cavani", "Eziquiel Lavezzi"]
print(f"{invitated_p}Ho trovato un tavolo più grande!!")
invitated_p.insert(0, "David Neres")
invitated_p.insert(len(invitated_p)//2, "Matteo Politano") #con len/2 inserisce l'elemento sempre al centro della lista, facendo appunto la lunghezza della lista /2, in caso di numeri con la virgola arrotonda per difetto
invitated_p.append("Alessandro Buongiorno")
print(f"{invitated_p[0]} siete invitati alla cena, non mancate!!")
print(f"{invitated_p[1]} siete invitati alla cena, non mancate!!")
print(f"{invitated_p[2]} siete invitati alla cena, non mancate!!")
print(f"{invitated_p[3]} siete invitati alla cena, non mancate!!")
print(f"{invitated_p[4]} siete invitati alla cena, non mancate!!")
print(f"{invitated_p[5]} siete invitati alla cena, non mancate!!")
print(f"{invitated_p[6]} siete invitati alla cena, non mancate!!")
print(f"{invitated_p[7]} siete invitati alla cena, non mancate!!")