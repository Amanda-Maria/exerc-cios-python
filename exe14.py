# Declare uma variável ano com um valor inteiro representando um ano e
# imprima se ele é bissexto ou não. Um ano é bissexto se for divisível por 4,
# mas não divisível por 100, a menos que também seja divisível por 400.

ano = int(input('Digite um ano: '))

if (ano % 4 == 0 and ano % 100 !=0) or ano % 400 == 0:
    print('Ano bissexto')

else:
    print('Ano não bissexto')