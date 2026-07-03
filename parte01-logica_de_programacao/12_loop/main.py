# tratamento de exceção
try:
    n = int(input('Informe umm número inteirio: '))

    # laço de repetição
    while n >= 0:
        print(n)
        n -= 1
except:
    print('Não foi possível exibir a contagem.')