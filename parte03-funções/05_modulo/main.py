import modulo


modulo.limpar()

a = float(input("Digite o valor de 'a': ").replace(',', '.'))
b = float(input("Digite o valor de 'b': ").replace(',', '.'))

x = modulo.equacao_primeiro_grau(a, b)

modulo.limpar()
print(f"Valor de X é {x}.")