# 18) Declare uma variável idade com um valor numérico inteiro.
# Verifique se a idade está no intervalo de 18 a 65 anos (inclusive) e imprima
# "Elegível" ou "Não elegível" com base na verificação.


idade = int(input('Digite a sua idade: '))

if idade >=18 or idade ==65:
    print('Elegível')

else:
    print('Não elegível')