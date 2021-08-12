from bottle import route, run, response
from random import randrange
from horoscope import generate_prediction


@route("/generate")
def generate_something():

    response.headers['Access-Control-Allow-Origin'] = '*'
    return {
        'prediction': generate_prediction(),
        'num': randrange(1, 6)
    }


run(host="localhost", port=8080)
