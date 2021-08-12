from random import choice


def generate_prediction():
    first = ['Утром', 'Завтра', 'В полдень']
    second = ['ожидайте', 'будьте вниматеьлны к', 'забудьте', 'съешьте']
    third = ['гостей', 'людей', 'забытых знакомых', 'зонтиков', 'осадков']

    i = 0
    result = []
    while i < 5:
        g = choice(first) + ' ' + choice(second) + ' ' + choice(third) + '.'
        i += 1
    return g
