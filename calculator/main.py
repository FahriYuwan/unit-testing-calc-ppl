from get_input import get_input
from validate import validation_result
from compute import compute

def main():
    try:
        operand1, operand2, operator = get_input()
        # Validasi input
        validation_result(operand1, operand2, operator)
        # Proses perhitungan sesuai operator
        result = compute(int(operand1), int(operand2), operator)
        print(result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
