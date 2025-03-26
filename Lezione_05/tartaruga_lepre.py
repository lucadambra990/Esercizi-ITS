import random
lista_posizioni:list[int] = []
for i in range(1,71):
    lista_posizioni.append(i)

#mapping percentuale - lancio (1=10% -- 2=20% -- 3=30%....)
random_number= random.randint(1,10)
pos_lepre=lista_posizioni[0]
pos_turtle=lista_posizioni[0]

def position(p1,p2):
    if p1==p2:
        print("OUCH!")

def mossaTurtle():
    match random_number:
        case "Passo veloce" if 1<=random_number<=5:
            pos_turtle=lista_posizioni[+3]
        case "Scivolata" if 6<=random_number<=7:
            pos_turtle=lista_posizioni[-6]
            if pos_turtle < 1:
                pos_turtle=lista_posizioni[0]
        case "Passo lento" if 8<=random_number<=10:
            pos_turtle=lista_posizioni[+1]

def mossaLepre():
    match random_number:
        case "Riposo" if 1<=random_number<=2:
            pos_lepre=lista_posizioni[+0]
        case "Grande balzo" if 3<=random_number<=4:
            pos_lepre=lista_posizioni[+9]
        case "Grande scivolata" if random_number==5:
            pos_lepre=lista_posizioni[-12]
            if pos_lepre < 1:
                pos_lepre=lista_posizioni[0]
        case "Piccolo balzo" if 6<=random_number<=8:
            pos_lepre=lista_posizioni[+1]
        case "Piccola scivolata" if 9<=random_number<=10:
            pos_lepre=lista_posizioni[-2]
            if pos_lepre < 1:
                pos_lepre=lista_posizioni[0]


tick=0
percosoT= ["'_' , "] * 71
percosoL= ["'_' , "] * 71
T=1
H=1
print("BANG !!!!! AND THEY'RE OFF !!!!!")
while tick <=70:
    








    tick+=1
    

