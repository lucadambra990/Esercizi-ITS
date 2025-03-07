#Esercizio2
macchine_NS:int = int(input("Inserisci il numero di macchine provenienti dalla tratta nord/sud: "))
macchine_EO:int = int(input("Inserisci il numero di macchine provenienti dalla tratta est/ovest: "))
soglia:int = int(input("Inserire il valore soglia per ogni tratta: "))
tempo_prio:int = int(input("Inserire il tempo prioritario delle tratte: "))
if macchine_NS > soglia:
    if macchine_EO > soglia:
        tempo_NS = 50
        tempo_EO = 50
    else:
        tempo_NS = tempo_prio
        tempo_EO = 100- tempo_prio
else:
    if macchine_NS > soglia:
        tempo_NS = 100 - tempo_prio
        tempo_EO = tempo_prio       
    else:
        veicoli_tot = macchine_EO + macchine_NS
        tempo_NS:float = (macchine_NS/veicoli_tot)*100
        tempo_EO:float = 100 - tempo_NS
print(f"Il tempo per la tratta nord/sud è {tempo_NS:.2f}%")
print(f"Il tempo per la tratta est/ovest è {tempo_EO:.2f}%")