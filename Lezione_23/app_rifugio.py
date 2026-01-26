from flask import Flask, jsonify, url_for
from rifiugioAnimali import Shelter,Dog,Cat

Rifugio:Shelter = Shelter()

Cane:Dog=Dog("1","Bobby",1,2,"Pastore tedesco",False)
Gatto:Cat=Cat("1","Mizzi",3,3.5,"gomitolo",True)

Rifugio.add(Cane)
Rifugio.add(Gatto)

app = Flask(__name__)

@app.route('/')
def description():
    return jsonify({
        "descrizione": "Welcome",

        "links":{
            "animals":url_for("lista_animali")
        }
    })

@app.route('/animals', methods = ['GET'])
def lista_animali():
    return jsonify(Rifugio.list_all())