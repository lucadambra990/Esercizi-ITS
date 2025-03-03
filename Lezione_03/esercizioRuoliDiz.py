ruoli:dict[str, int] = {"nome":input("Inserisci il nome dell'utente: "), "ruolo":input("Inserisci il ruolo dell'utente: "), "età":int(input("Inserisci l'età dell'utente: "))}

match ruoli:
    case {"nome":name, "ruolo":"Admin"}:
        print("Accesso completo a tutte le funzionalità")
    case {"nome":name, "ruolo":"Moderatore"}:
        print("Può gestire i contenuti ma non modificare le impostazioni")
    case {"nome":name, "ruolo":"Utente adulto","età":eta} if eta>=18:
        print("Accesso standard a tutti i servizi")
    case {"nome":name, "ruolo":"Utente minorenne", "età":eta} if eta<18:
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case {"nome":name, "ruolo":"Ospite"}:
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Ruolo non riconosciuto! Accesso negato.")