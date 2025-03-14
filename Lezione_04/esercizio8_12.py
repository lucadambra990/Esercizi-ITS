ingredients:list[str] = []
def make_sandwich(ingredients:list):
    while True:
        elem:str=input("Inserisci gli elementi che compongono il panino: ")
        if elem=="esci":
            break
        ingredients.append(elem)
    print(f"Gli ingredienti del tuo panino sono:\n{ingredients}")
make_sandwich(ingredients)