import mycalc


def test_add():
    assert mycalc.add(1, 2) == 3


def test_mul():
    assert mycalc.mul(2, 5) == 10


def test_sub():
    if mycalc.sub(4, 2) == 2:
        print('sub(a, b) OK')
    else:
        print('sub(a, b) NOT OK')


def test_div():
    if mycalc.div(8, 4) == 2:
        print('div(a, b) OK')
    else:
        print('div(a, b) NOT OK')


def test_sqtr():
    if (mycalc.sqrt(9) - 3) < .000000001:
        print('sqrt(a, b) OK')
    else:
        print('sqrt(a, b) NOT OK')


try:
    test_add()
    print('add(a, b) OK')
except AssertionError:
    print('add(a, b) NOT OK')

try:
    test_mul()
    print('mul(a, b) OK')
except AssertionError:
    print('mul(a, b) NOT OK')

test_sub()
test_div()
test_sqtr()
