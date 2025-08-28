def massimo(a,b,c):
    if a>b and a>c:
        return f"Il numero {a} è il massimo"
    if b>a and b>c:
        return f"Il numero {b} è il massimo"
    if c>a and c>b:
        return f"Il numero {c} è il massimo"
    
print(massimo(11,25,3))
# versione alternativa con max
def massimo_max(a, b, c):
    massimo_val = max(a, b, c)
    return massimo_val  

print(massimo_max(11,25,3))
