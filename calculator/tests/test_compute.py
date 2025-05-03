from calculator.compute import compute

def test_compute():
    assert compute(10, 10, "+") == "Hasil: 20"
    assert compute(10, 10, "-") == "Hasil: 0"
    assert compute(10, 10, "*") == "Hasil: 100"
    assert compute(10, 10, "/") == "Hasil: 1.0"
