lista_messaggi:list = ["Ciao","Come stai?","Tutto bene?","A presto!"]

def show_message(lista_messaggi:list):
    print(lista_messaggi)
    copy_message:list[str] = []
    copy_message.append(lista_messaggi)
    return copy_message
print(show_message(lista_messaggi))