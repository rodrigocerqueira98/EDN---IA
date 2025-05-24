# Calculadora tratamento de erros
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
        continue

    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao not in ['+', '-', '*', '/']:
        print("Erro: Operação inválida. Use apenas +, -, * ou /.")
        continue

    try:
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        continue

    print(f"Resultado: {resultado}")
    break
