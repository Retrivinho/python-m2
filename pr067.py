while True:
    n = int(input('Quer ver a tabuada de qual número ?  ' ))
    print('-=' * 25)
    if n < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n*c))
    print('-=' * 25)

print('PROGRAMA DE TABUADA ENCERRADO !!')





