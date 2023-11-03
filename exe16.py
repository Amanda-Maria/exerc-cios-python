# 16) Declare duas variáveis, idade1 e idade2, com valores inteiros.
# Verifique se pelo menos uma das idades é maior ou igual a 18
# e imprima "Pelo menos uma pessoa é maior de idade" ou "Nenhuma pessoa é maior de idade"
# com base na verificação.


idade1 = int(input('Digite a primeira idade: '))
idade2 = int(input('Digite a segunda idade: '))

if idade1 >=18 or idade2 >= 18:
    print('Pelo menos uma pessoa é maior de idade')

else:
    print('Nenhuma pessoa é maior de idade')

