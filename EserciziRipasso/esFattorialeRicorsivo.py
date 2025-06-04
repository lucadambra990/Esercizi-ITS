def fattoriale(n)->int:
    if n==1:
        return 1
    else:
        return n * fattoriale(n-1)

print(fattoriale(5))