from bottle import route, run, response
from random import choice, randrange


@route("/generate")
def generate_something():
    first = ['Утром', 'Завтра', 'В полдень']
    second = ['ожидайте', 'будьте вниматеьлны к', 'забудьте', 'съешьте']
    third = ['гостей', 'людей', 'забытых знакомых', 'зонтиков', 'осадков']

    i = 0
    result = []
    while i < 5:
        g = choice(first) + ' ' + choice(second) + ' ' + choice(third) + '.'
        i += 1
        response.headers['Access-Control-Allow-Origin'] = '*'
    return {
        'prediction': g,
        'num': randrange(1, 6)
    }





run()
