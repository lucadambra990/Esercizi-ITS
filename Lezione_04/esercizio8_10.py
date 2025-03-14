lista_messaggi:list = ["Ciao","Come stai?","Tutto bene?","A presto!"]

def send_messages(messaggi:str):

    sent_messages:str = []
    val_massimo = len(messaggi)
    print(f"{messaggi=}\n{sent_messages=}\n\n")
    for i in range(val_massimo):
        message=messaggi.pop(0)
        sent_messages.append(message)
        print(f"{messaggi=}\n{sent_messages=}\n\n") #= fa vedere il nome è il contenuto

send_messages(lista_messaggi)