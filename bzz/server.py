from bottle import route, run
from random import choice


@route("/")
def my_func():
    return "OK"


@route("/jdva")
def my_func():
    return {
        "my_saying": {
            "test": "ываываываываываываы",
            "test2": choice(
                ["awdeaqw", 2, "awdaw", 80]
            ),
        }
    }

run()
