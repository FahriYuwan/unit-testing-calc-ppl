from calculator.get_input import get_input

def test_input():
    operand1, operand2, operator = get_input()
    assert operand1 == '1'
    assert operand2 == '2'
    assert operator == '+'
