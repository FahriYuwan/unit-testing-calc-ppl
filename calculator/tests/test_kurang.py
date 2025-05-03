from calculator.calculate import kurang

def test_kurang():
    assert kurang(0,0) == 0
    assert kurang(0,4) == -4
    assert kurang(0,-4) == 4
    assert kurang(4,0) == 4
    assert kurang(-4,0) == -4
    assert kurang(-4,-4) == 0
    assert kurang(4,4) == 0