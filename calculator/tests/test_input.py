from calculator.get_input import get_input

def test_input(monkeypatch):
    inputs = iter(['1', '2', '+'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    operand1, operand2, operator = get_input()
    
    assert operand1 == '1'
    assert operand2 == '2'
    assert operator == '+'