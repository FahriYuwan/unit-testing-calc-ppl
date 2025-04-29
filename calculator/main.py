from calculator.get_input import get_input
from calculator.validate import validate_input
from calculator.compute import compute

def main():
    try:
        operand1, operand2, operator = get_input()
        # Validasi input
        validation_result = validate_input(operand1, operand2, operator)
        if validation_result:
            print(validation_result)
            return
        # Proses perhitungan sesuai operator
        result = compute(int(operand1), int(operand2), operator)
        print(result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
