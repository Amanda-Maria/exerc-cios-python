# 12) Declare uma variável nota com um valor numérico representando uma nota em uma escala de 0 a 10. 
# Verifique se a nota é maior ou igual a 7 e imprima "Aprovado" ou "Reprovado" com base na verificação

nota = int(input('Digite a sua nota: '))

if nota >= 7:
    print('Aprovado')

else:
    print('Reprovado')