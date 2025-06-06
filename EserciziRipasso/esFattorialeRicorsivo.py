def fattoriale(n)->int:
    if n==1:
        return 1
    else:
        return n * fattoriale(n-1)

print(fattoriale(5))

# funzione tutta in una riga -- return 1 if n==1 else n*fattoriale(n-1)