from flask import Flask
import data, random

app = Flask(__name__)

def random_card(deck):
    return {"card": random.choice(deck)}

@app.route("/level1")
def l1():
    return random_card(data.levelOne)

@app.route("/level2")
def l2():
    return random_card(data.levelTwo)

@app.route("/level3")
def l3():
    return random_card(data.levelThree)

if __name__ == "__main__":
    app.run(threaded=True, port=8000)