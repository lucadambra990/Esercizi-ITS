# dal modulo esercizio12_1.py importare la classe MovieCatalog
from esercizio12_1 import MovieCatalog

# creare un oggetto della classe MovieCatalog
catalog:MovieCatalog=MovieCatalog()

# aggiungiamo un registra e dei film al catalogo
catalog.add_movie("Steven Spielberg",["Casper","Ritorno al futuro"])

# print(catalog.getCatalog())

# aggiungere un altro film di Spielberg al catalogo

catalog.add_movie("Steven Spielberg",["ET"])
# print(catalog.getCatalog())

# aggiungere un nuovo regista
catalog.add_movie("Quentin Tarantino",["Pulp Fiction", "Kill Bill"])

# print(catalog.getCatalog())

# rimuovere il film ET dal catalogo
catalog.remove_movie("Steven Spielberg", "ET")

catalog.remove_movie("Steven Spielberg", "Ritorno al futuro")

catalog.remove_movie("Steven Spielberg", "Casper")

print(catalog.getCatalog())

print(catalog.list_directors())