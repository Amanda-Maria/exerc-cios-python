# 17) Declare uma variável palavra com uma string e verifique se
# a primeira letra da palavra é igual à última letra. Imprima "Sim" ou "Não" com base na verificação.


palavra = input('Escreva uma palavra: ')

if palavra[0] == palavra[-1]:
    print('Sim')

else:
    print('Não')