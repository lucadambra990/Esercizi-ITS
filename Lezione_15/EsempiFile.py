import json

encoding:str="utf-8"

PATH:str = "info.json"
with open(PATH, mode="r",encoding=encoding) as file:
    config:dict = json.load(file)

with open(PATH,mode="w") as file:
    json.dump(config,file,indent=4) # permette di salvare un dizionario come un file json