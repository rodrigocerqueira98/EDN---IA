
# 2 - Calculadora de Desconto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20  # em %

valor_desconto = round(preco_original * (porcentagem_desconto / 100), 2)
preco_final = round(preco_original - valor_desconto, 2)

print("\nProduto:", nome_produto)
print("Preço original: R$", preco_original)
print("Desconto:", porcentagem_desconto, "%")
print("Valor do desconto: R$", valor_desconto)