qtd = 0
soma = 0
media = 0

valor = float(input("Digite um valor: "))

while valor > 0.0:
    soma += valor  # Soma acumulativa
    qtd += 1  # Contador de valores positivos

    # Entrada de novos valores
    valor = float(input("Digite um valor: "))

# Caso o usuário não tenha digitado nenhum valor positivo, evita erro de divisão por zero
if qtd > 0:
    media = soma / qtd
    print("\nTotal da Soma:", soma)
    print("Quantidade de valores digitados:", qtd)
    print("Média dos valores:", media)
else:
    print("\nNenhum valor positivo foi digitado.")