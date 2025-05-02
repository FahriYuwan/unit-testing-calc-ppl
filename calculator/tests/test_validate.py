import pytest
from calculator.validate import validate_input, validation_result

def test_validate_input_valid():
    # Test valid input
    assert validate_input(10, 5, "+") is None
    assert validate_input(-32768, 32767, "-") is None


def test_validate_input_non_numeric():
    # Test invalid input (non-numeric)
    assert validate_input("abc", 5, "+") == "Error: operand harus angka"
    assert validate_input(5, "abc", "+") == "Error: operand harus angka"
    assert validate_input("abc", "xyz", "*") == "Error: operand harus angka"


def test_validate_input_out_of_range():
    # Test invalid input (out of range)
    assert validate_input(40000, 5, "+") == "Error: operand harus berada pada range -32768 hingga 32767"
    assert validate_input(10, 40000, "-") == "Error: operand harus berada pada range -32768 hingga 32767"
    assert validate_input(-40000, 5, "*") == "Error: operand harus berada pada range -32768 hingga 32767"


def test_validate_input_invalid_operator():
    # Test invalid operator
    assert validate_input("10", "5", "%") == "Error: operator tidak valid. Operator yang diperbolehkan adalah +, -, *, /"
    assert validate_input(10, 5, "^") == "Error: operator tidak valid. Operator yang diperbolehkan adalah +, -, *, /"


def test_validate_input_division_by_zero():
    # Test division by zero
    assert validate_input("10", "0", "/") == "Error: pembagi tidak boleh nol"
    assert validate_input(10, 0, "/") == "Error: pembagi tidak boleh nol"


def test_validation_result_valid():
    # Test valid input
    assert validation_result(10, 5, "+") is None
    assert validation_result(-32768, 32767, "-") is None


def test_validation_result_non_numeric():
    # Test invalid input (non-numeric)
    with pytest.raises(SystemExit) as excinfo:
        validation_result("abc", 5, "+")
    assert excinfo.value.code == 1
    with pytest.raises(SystemExit) as excinfo:
        validation_result(5, "xyz", "*")
    assert excinfo.value.code == 1