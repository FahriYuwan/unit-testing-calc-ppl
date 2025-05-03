from calculator.calculate import tambah

def test_tambah():
    assert tambah(0,0) == 0
    assert tambah(0,4) == 4
    assert tambah(0,-4) == -4
    assert tambah(-4,-4) == -8
    assert tambah(4,4) == 8