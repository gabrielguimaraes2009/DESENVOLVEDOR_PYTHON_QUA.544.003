países = {
    "Brasil",
    'Estados Unidos', 
    'México', 
    'Argentina', 
    'Árabia Saudita', 
    'Brasil', 
    'Irã', 
    'Brasil', 
    'Estados Unidos', 
    'Brasil'
}

país = input("Informe o país a ser pesquisado: ").strip().title()

# armazena a quantidade de ocorrências na lista
qtde = paises.count(paises)

print(f'{país} foi encontrado {qtde} vezes na lista.')