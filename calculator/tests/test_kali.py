from calculator.calculate import kali

def test_kali():
    assert kali(10,10) == 100
    assert kali(-10,-10) == 100
    assert kali(-10,10) == -100
    assert kali(0,10) == 0
    assert kali(0,-10) == 0