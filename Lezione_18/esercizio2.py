def validate_password(password:str):
    #minimo 20 caratteri
    #almeno 3 lettere maiuscole
    #almeno 4 caratteri speciali non alfanumerici
    if len(password)<20:
        raise ValueError(f"La passwordo è troppo corta")
    for i in password:
        if i is upper:
            raise ValueError(f"La password non rispetta i criteri")
        
validate_password("hahahahfshhhhouahgvoushgoub")