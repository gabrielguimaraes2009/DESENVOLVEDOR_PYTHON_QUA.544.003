nomes = [
    "Fulano", 
    'Ciclano', 
    'Beltrano', 
    'João', 
    'Maria', 
    'José', 
    'Esmeralda'
]

nome = input('Informe o nome a ser deletado:').strip().title()

if nome in nomes:
    indice = nome.index(nome)

    # apaga a nova lista sem o item deletado
    for nome in nomes:
        print(nomes)
else:
    print('Não encontrado')