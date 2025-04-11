def validate_password(password:str):
    #minimo 20 caratteri
    #almeno 3 lettere maiuscole
    #almeno 4 caratteri speciali non alfanumerici
    if len(password)<20:
        raise ValueError(f"La passwordo è troppo corta")
    for i in password:
        is_upper=0
        if i.isupper():
            is_upper+=1
        if is_upper < 3:
            raise ValueError(f"La password non rispetta i criteri")
        is_special=0
        not_special=0
        if i.isalpha() or i.isnumeric():
            not_special+=1
        else:
            is_special+=1
        if is_special < 4:
            raise ValueError(f"La password non ha abbastana caratteri speciali") 

        
validate_password("hahahahfshhhhouahgvoushgoub")