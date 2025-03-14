def make_cars(model:str,produtture:str):
    car:dict={"model":model,"produttore":produtture}
    color:str="blue"
    tow:bool = True
    car["color"]=color
    car["tow"]=tow
    return car

if __name__=="__main__":
    car=print(make_cars("BMW m4","BMW"))
