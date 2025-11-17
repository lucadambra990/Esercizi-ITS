from flask import Flask, jsonify, request

from db.utils import load_data_from_db, store_data_on_db

app = Flask(__name__)

@app.route('/')
def initial_message():
    return jsonify({"response":'Questo è il messaggio di benvenuto'})

@app.route('/nazioni', methods=['GET'])
def get_nazioni():
    dati = load_data_from_db() # Carica TUTTI i dati dal finto database nel file json
    nazioni: dict[str, dict[str, str]] = dati['Nazione']
    return jsonify(nazioni), 200

@app.route('/nazioni/<string:nome>',methods=['GET'])
def get_nazione87(nome:str):
    dati = load_data_from_db()
    if nome not in dati['Nazione']:
        return jsonify({'error': f"La nazione {nome} non esiste!"})
    nazione:dict[str,str] = dati['Nazione'][nome]
    return jsonify(nazione),200

@app.route('/all',methods=['GET'])
def get_all():
    dati = load_data_from_db()
    return jsonify(dati),200

@app.route('/citta',methods=['GET'])
def get_citta():
    dati = load_data_from_db()
    citta:dict[str, dict[str,str|int]] = dati['Citta']
    return jsonify(citta),200

@app.route('/citta/<int:id_citta>',methods=['GET'])
def get_cittaById(id_citta:int):
    dati = load_data_from_db()
    citta:dict[str, dict[str,str|int]] = dati['Citta']
    cittaById = citta[str(id_citta)]
    return jsonify(cittaById),200

@app.route('/aereoporto',methods=['GET'])
def get_aereoporto():
    dati = load_data_from_db()
    aereoporto:dict[str, dict[str,str|int]] = dati['Aereoporto']
    return jsonify(aereoporto),200

@app.route('/compagnia',methods=['GET'])
def get_compagnia():
    dati = load_data_from_db()
    compagnia:dict[str, dict[str,str|int]] = dati['Compagnia']
    return jsonify(compagnia),200

@app.route('/volo',methods=['GET'])
def get_volo():
    dati = load_data_from_db()
    volo:dict[str, dict[str,str|int]] = dati['Volo']
    return jsonify(volo),200

@app.route('/nazioni', methods=['POST'])
def add_nazione():
    new_nazione = request.get_json()
    if "nome" not in new_nazione:
        return jsonify({"errore": "Per creare una nazione, fornire il nome!"}),400
    nazioni = load_data_from_db()['Nazione']
    if new_nazione["nome"] in nazioni:
        return jsonify({"errore":f"Esiste già una nazione con nome {new_nazione['nome']}!"}),400
    
    dati=['Nazione'][new_nazione["nome"]] = new_nazione
    store_data_on_db(dati)
    return jsonify(new_nazione),200

if __name__ == "__main__":
    app.run(debug=True)