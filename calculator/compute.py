from calculate import tambah, kurang, kali, bagi

def compute(operand1, operand2, operator):
    if operator == '+':
        return f"Hasil: {tambah(operand1, operand2)}"
    elif operator == '-':
        return f"Hasil: {kurang(operand1, operand2)}"
    elif operator == '*':
        return f"Hasil: {kali(operand1, operand2)}"
    elif operator == '/':
        return f"Hasil: {bagi(operand1, operand2)}"