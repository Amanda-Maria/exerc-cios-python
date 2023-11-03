# 15) Declare uma variável preco_produto com um valor numérico e uma variável desconto com um
# valor numérico representando um desconto percentual. Calcule o preço com desconto e imprima-o.


preco_produto = int(input('Digite o preço do produto: '))
preco_desconto = int(input('Digite o valor do desconto: '))

preco_final = preco_produto * (1 - preco_desconto/100)

print(f'Preço final com desconto é de: {preco_final:.2f}')



# A razão para usar (1 - desconto/100) é que
# o desconto é representado como uma porcentagem,
# e para calcular o valor do desconto em reais,
# você precisa converter essa porcentagem em uma fração decimal.
# Normalmente, os descontos são aplicados subtraindo uma determinada porcentagem do preço original,
# e essa porcentagem é dividida por 100 para obter a fração decimal equivalente.

