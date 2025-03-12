def calcular_media(nota1, nota2):
    """Calcula a média de duas notas e retorna a situação do aluno."""
    media = (nota1 + nota2) / 2

    if media >= 7.0:
        return media, "APROVADO "
    else:
        return media, "REPROVADO "


# Entrada de notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Chamada da função
media, situacao = calcular_media(nota1, nota2)

# Exibição do resultado
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")