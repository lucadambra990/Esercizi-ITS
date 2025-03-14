def build_profile(first_name:str,last_name:str,age:int,weight:float,characteristic:str):
    return {"first_name":first_name,"last_name":last_name,"age":age,"weight":weight,"characteristic":characteristic}.values()


print(build_profile("Luca","D'Ambra",21,72.5,"brown hair"))