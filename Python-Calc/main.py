def main():
    try:
        operand1 = input("Masukkan operand pertama: ")
        operand2 = input("Masukkan operand kedua: ")
        operator = input("Masukkan operator (+, -, *, /): ")
        from computation import compute
        result = compute(operand1, operand2, operator)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
