NUMBERS = [1, 2, 3]
SYMBOLS = ['DIAMONDS', 'SQUIGGLE', 'OVAL']
SHADINGS = ['STRIPPED', 'SOLID', 'OPEN']
COLORS = ['RED', 'GREEN', 'PURPLE']


class Card:
    def __init__(self, number, symbol, shading, color):
        if any([
            number not in NUMBERS,
            symbol not in SYMBOLS,
            shading not in SHADINGS,
            color not in COLORS
        ]):
            raise ValueError('Неправильные параметры карты')
        self.number = number
        self.symbol = symbol
        self.shading = shading
        self.color = color


NMBERS = [4, 5, 6]
cards = (NUMBERS, SYMBOLS, SHADINGS, COLORS)


def check_set(cards):
    if cards[0] is NUMBERS and cards[1] is SYMBOLS and cards[2] is SHADINGS and cards[3] is COLORS:
        print('Set is valid')
        return True
    else:
        print('Set is invalid')
        return False


check_set(cards)
