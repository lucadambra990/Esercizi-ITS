def dictPrice(dictP:dict[str:float])->dict:
    dict2:dict={}
    for key, value in dictP.items():
        if value <= 50:
            value=round(value+(value*0.1),2)
            dict2[key]=value
    return dict2

print(dictPrice({"Monster":2.50,"Deodorante":1.50,"Don Perignon":60.35}))

