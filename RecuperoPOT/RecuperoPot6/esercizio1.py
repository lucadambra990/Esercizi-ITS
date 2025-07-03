def recursivePalindrome(parola:str)->bool:
    parola = parola.lower().replace(" ","")
    if len(parola)<=1:
        return True
    if parola[0] == parola[-1]:
        return recursivePalindrome(parola[1:-1])
    else:
        return False
    
print(recursivePalindrome("Anna"))