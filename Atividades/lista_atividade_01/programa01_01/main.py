nome = input('Informe o nome:')
altura = float(input('Informe a altura:').replace(',', ','))
peso = float(input('Informe o peso:').replace(',', ','))

imc = peso/altura**2

print(f'{nome} seu IMC é {imc}')

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
elif imc < 35:
    print("Classificação: Obesidade grau I")
elif imc < 40:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III")