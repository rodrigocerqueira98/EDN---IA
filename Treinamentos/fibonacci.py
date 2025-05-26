def fibonacci(n):
    a, b = 0, 1  # Começa a sequência com 0 e 1
    for _ in range(n):  # Repete n vezes
        print(a, end=" ")  # Mostra o número atual da sequência
        a, b = b, a + b  # Atualiza os valores: o próximo é a soma dos dois anteriores

# Solicita ao usuário a quantidade de números da sequência
quantidade = int(input("Quantos números da sequência de Fibonacci você quer ver? "))

# Chama a função com a quantidade informada
fibonacci(quantidade)
