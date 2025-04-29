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