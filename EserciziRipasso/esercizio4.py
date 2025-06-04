def condition(x:int|float,y:int|float,z:int|float)->str:
    if x>y and z>y:
        return "Azione Permessa"
    else:
        return "Azione negata"
        
print(condition(10,20,30))
