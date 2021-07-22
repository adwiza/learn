from bottle import route, run
from random import choice


@route("/")
def my_func():
    return "OK"




run()
