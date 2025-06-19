import string
def Parole(stringa:str)->dict:
    word_dict:dict={}
    for token in stringa.split():
        token = token.lower().strip(string.punctuation)
        if not token:
            continue
        if token in word_dict:
            pass
    return word_dict




print(Parole("aaaaaaaaaaavvvvvvvvvvvvvvvvvvvvv"))

            

