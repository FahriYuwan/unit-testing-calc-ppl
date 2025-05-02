import pytest
from calculator.validate import validate_input, validation_result

def test_validate_input():
    # Test valid input
    assert validate_input(10, 5, "+") is None

    # Test invalid input (non-numeric)
    assert validate_input("abc", 5, "+") == "Error: operand harus angka"
    assert validate_input(5, "abc", "+") == "Error: operand harus angka"

    # Test invalid input (out of range)
    assert validate_input(40000, 5, "+") == "Error: operand harus berada pada range -32768 hingga 32767"
    assert validate_input(10, 40000, "-") == "Error: operand harus berada pada range -32768 hingga 32767"

    # Test invalid operator
    assert validate_input("10", "5", "%") == "Error: operator tidak valid. Operator yang diperbolehkan adalah +, -, *, /"

    # Test division by zero
    assert validate_input("10", "0", "/") == "Error: pembagi tidak boleh nol"

def test_validation_result():
    # Test valid input
    assert validation_result(10, 5, "+") is None

    # Test invalid input (non-numeric)
    with pytest.raises(SystemExit) as excinfo:
        validation_result("abc", 5, "+")
    assert excinfo.value.code == 1