def get_input():
    operand1 = input("Masukkan operand pertama: ")
    operand2 = input("Masukkan operand kedua: ")
    operator = input("Masukkan operator (+, -, *, /): ")
    return operand1, operand2, operator

def validate_input(operand1, operand2, operator):
    try:
        num1 = int(operand1)
        num2 = int(operand2)
    except ValueError:
        return "Error: operand harus angka"

    # Validasi range
    if not (-32768 <= num1 <= 32767) or not (-32768 <= num2 <= 32767):
        return "Error: operand harus berada pada range -32768 hingga 32767"

    # Validasi operator
    if operator not in ['+', '-', '*', '/']:
        return "Error: operator tidak valid. Operator yang diperbolehkan adalah +, -, *, /"

    # Validasi pembagi pada operasi bagi
    if operator == '/' and num2 == 0:
        return "Error: pembagi tidak boleh nol"

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

def compute(operand1, operand2, operator):
    if operator == '+':
        return f"Hasil: {tambah(operand1, operand2)}"
    elif operator == '-':
        return f"Hasil: {kurang(operand1, operand2)}"
    elif operator == '*':
        return f"Hasil: {kali(operand1, operand2)}"
    elif operator == '/':
        return f"Hasil: {bagi(operand1, operand2)}"

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
