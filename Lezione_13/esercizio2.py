def compoundInterest(m:float, t:int) ->float:
    #if m is negative
    if m<0.00:
        print("La somma è negaiva")
        return 0.00
    #if m is 0, the compound interest is 0
    elif m==0:
        return 0.00
    #m must be >0
    else:
        #if t is negative or 0, it means that no month has passed yet, so balance is 0
        if t<=0:
            return round(m,2)
        # calculate the compound interest recursively
        else:
            return round(1.005*compoundInterest(m,t-1),2)
        
print(compoundInterest(2000,5))