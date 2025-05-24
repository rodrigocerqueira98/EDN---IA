
# Verificador de senha forte
while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    tem_numero = any(char.isdigit() for char in senha)
    if len(senha) >= 8 and tem_numero:
        print("Senha válida e forte!")
        break
    else:
        print("Senha fraca! Deve ter ao menos 8 caracteres e conter um número.")

