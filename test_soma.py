from soma import soma


def test_soma_numeros_positivos():
    assert soma(2, 3) == 5


def test_soma_com_negativos():
    assert soma(-2, -3) == -5


def test_soma_com_zero():
    assert soma(0, 7) == 7
