import sys
import pytest

try:
    import pandas as pd
except ImportError:
    pass


@pytest.mark.skipif(
    'pandas' not in sys.modules,
    reason='Нужна библиотека Pandas для теста'
)
def test_somethiong():
    print('All fine')
