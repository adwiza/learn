from bottle import route, run
from random import choice, randrange


def generate_some():
    first = ['Утром', 'Завтра', 'В полдень']
    second = ['ожидайте', 'будьте вниматеьлны к', 'забудьте', 'съешьте']
    third = ['гостей', 'людей', 'забытых знакомых', 'зонтиков', 'осадков']

    i = 0
    result = []
    while i < 5:
        g = choice(first) + ' ' + choice(second) + ' ' + choice(third) + '.'
        i += 1
        result.append(g)
    return {
        'prophecies': result,
    }