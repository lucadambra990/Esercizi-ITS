from flask import Flask, jsonify, request, url_for
from parcoDivertimenti import Park, RollerCoaster, Carousel

app = Flask(__name__)

parco = Park()

parco.add(RollerCoaster(1, "Fire", 160, 6))
parco.add(Carousel(2, "Ice", 150, ["tiger", "lion", "zebra"]))


@app.route("/")
def description():
    return jsonify({
        "descrizione": "Welcome to the Naples Park",
        "links": {
            "attrazioni": url_for("list_park"),
        }
    })


@app.route("/parco", methods=["GET"])
def list_park():
   # return jsonify([ride.info() for ride in parco.list_all()])
   return jsonify(parco.list_all())

@app.route("/parco/rollercoaster", methods=["POST"])
def add_rollercoaster():
    payload = request.json

    rollercoaster = RollerCoaster(
        payload["id"],
        payload["name"],
        payload["min_height_cm"],
        payload["inversions"]
    )
    parco.add(rollercoaster)
    return rollercoaster.info(), 201

@app.route("/parco/carousel", methods=["POST"])
def add_carousel():
    payload = request.json

    carousel = Carousel(
        payload["id"],
        payload["name"],
        payload["min_height_cm"],
        payload["animals"]
    )

    parco.add(carousel)
    return carousel.info(), 201

