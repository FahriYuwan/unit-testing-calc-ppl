from calculator.calculate import bagi

def test_bagi():
    assert bagi(10,10) == 1.0
    assert bagi(-10,-10) == 1.0
    assert bagi(-10,10) == -1.0
    assert bagi(0,10) == 0
    assert bagi(0,-10) == 0
