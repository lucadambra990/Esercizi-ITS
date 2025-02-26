color:str = input("Inserisci un colore: ")
predict:bool

if color == "red".lower():
    predict=True
    print(f"{color.lower()} == color? {predict}")
else:
    predict=False
    print(f"Predict {predict}")