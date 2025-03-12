def make_shirt(size:str, msg:str):
    print(f"La taglia della maglia è {size}, il mesaggio che verrà stampato sopra è {msg}")

    
print("Parametri della funzione passati per posizione")
make_shirt("L", "\"Forza Napoli\"")
print("Parametri della funzione passati per keyword")
make_shirt(size="L", msg="\"Forza Napoli\"")