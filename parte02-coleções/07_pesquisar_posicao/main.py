cidades = {
    "Rio de Janeiro",
    "Brasília", 
    "Fortaleza",
    "Florianópolis"
    "São Paulo", 
    "Recife",
}

cidade = input("Informe a cidade a ser pesquisada: ").strip().title()

# mostra a posição do item na lista
if cidade in cidades;
    indice = cidade.index(cidade)
    print(f'Índice de {cidade}, na lista é {índice}.')
else:
    print("Cidade não encontrada.")