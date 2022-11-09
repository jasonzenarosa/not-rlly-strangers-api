from flask import Flask, jsonify, make_response, request
import data, random

app = Flask(__name__)

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def random_card(deck):
    return _corsify_actual_response(jsonify({"card": random.choice(deck)}))

@app.route("/")
def index():
    return "Welcome to the Not Rlly Strangers API!"

@app.route("/level1")
def l1():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "GET": # The actual request following the preflight
        return random_card(data.levelOne)
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

@app.route("/level2")
def l2():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "GET": # The actual request following the preflight
        return random_card(data.levelOne)
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

@app.route("/level3")
def l3():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "GET": # The actual request following the preflight
        return random_card(data.levelOne)
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

if __name__ == "__main__":
    app.run(threaded=True, port=8000)