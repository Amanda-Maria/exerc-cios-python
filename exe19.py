# 19) Declare uma variável salario com um valor numérico e uma variável idade com um valor numérico inteiro.
# Verifique se o salário é maior ou igual a 1000 e a idade é maior ou igual a 18.
# Imprima "Elegível" ou "Não elegível" com base na verificação.


salario = int(input('Digite o seu salário: '))
idade = int(input('Digite sua idade: '))

if salario >= 1000 and idade >=18:
    print ('Elgível')

else:
    print('Não elegível')