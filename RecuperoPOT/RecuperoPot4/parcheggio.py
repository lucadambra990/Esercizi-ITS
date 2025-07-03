import math
from typing import Any
def calculateCharges(ore:float)-> int:
    tar:float = 0.0
    if ore < 3:
        tar = 2
    else:
        if ore > 3 and ore < 24:
            if ore%1!=0:
               ore = math.ceil(ore)
            tar = 2.00+(ore-3)*0.5
        else:
            tar = 10
    return tar

listaTot:list[Any] = [1.5,4.0,5.5,24.0]
tot = 0

print(f"{'Car':<10} {'Hours':<10} {'Charge':<10}")

for i in range(len(listaTot)):
    t = calculateCharges(listaTot[i])
    print(f"{i+1:<10} {listaTot[i]:<10} {t:<.2f}")
    tot += t
print(f"{'TOTAL':<10} {sum(listaTot):<10} {tot:<.2f}")
