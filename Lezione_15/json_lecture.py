import json

PATH:str = "db.json"
mode:str = "r"
encoding:str="utf-8"


config=None

with open(PATH,mode=mode,encoding=encoding) as file:

   config:dict = json.load(file)


config["AGGIUNTA"] = "NUOVO"
config["dati_persona"]["nome"] = "Gigio"

with open(PATH, mode="w") as file:
   json.dump(config, file, indent=4) #indent = numero di spazi
   