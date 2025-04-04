def blackjack_hand_total(cards: list[int]) -> int: 
    somma:int = 0
    aces:int = 0
    for i in cards:
        if i==11:
            aces+=1
            somma+=i
        else:
            somma+=i
        while somma > 21 and aces > 0:
            somma-=10
    return somma