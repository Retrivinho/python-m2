print('-=' * 20)
print('Analisador de Triagulos')
print('-=' * 20)
r1 = float(input('Digite a medida do primerio segmento: '))
r2 = float(input('Digite a medida do segundo seguimento: '))
r3 = float(input('Digite a medida do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima POREM FORMAR UM TRIÂGULO ! ')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR UM TRIÂNGULO ! ')

