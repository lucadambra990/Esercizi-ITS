def check_lenght(mystr:str):
    if len(mystr) > 10:
        print(f"La lunghezza della stringa inserita è maggiore di 10, len={len(mystr)}")
    elif len(mystr)<10:
        print(f"La lunghezza della stringa inserita è minore di 10, len={len(mystr)}")
    else:
        print(f"La lunghezza della stringa inserita è uguale a 10, len={len(mystr)}")

check_lenght("Ciao, sono Luca")