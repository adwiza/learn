import random

import pytest

import mycalc


# pytest.skip('Не надо проверять калькулятор', allow_module_level=True)
# @pytest.mark.skip('Нет никаких сложений')
def test_add():
    # pytest.skip('Нет никаких с2ложений')
    assert mycalc.add(1, 2) == 3


@pytest.mark.skipif(random.random() < .5,
                    reason='Умножению не повезло')
def test_mul():
    assert mycalc.mul(3, 7) == 21


def test_sub():
    assert mycalc.sub(4, 2) == 2


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_div():
    # with pytest.raises(ZeroDivisionError):
    mycalc.div(1, 0)


def test_sqtr():
    assert (mycalc.sqrt(9) - 3) < .000000001
