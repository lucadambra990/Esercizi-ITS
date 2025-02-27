lista_oggetti:list[any] = []
for i in range(0,3):
    oggetto:str = input("Inserisci un oggetto nella lista: ")
    lista_oggetti.append(oggetto)

match lista_oggetti:
    case["penna","matita","quaderno"]:
        print("Materiale scolastico")
    case["pane","latte","uova"]:
        print("Prodotti alimentari")
    case["sedia","tavolo","armadio"]:
        print("Mobili")
    case["telefono","computer","tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")
print(lista_oggetti)