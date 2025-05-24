
# Registro de notas e calculos de média

notas = []

while True:
    entrada = input("Digite a nota (ou 'fim' para encerrar): ").strip().lower()
    if entrada == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Insira um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número válido ou 'fim'.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
