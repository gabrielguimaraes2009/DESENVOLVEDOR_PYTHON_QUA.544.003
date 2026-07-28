nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

filmes = {
    1: ("A Volta dos Que Não Foram", 0),
    2: ("A Roda Quadra", 12),
    3: ("As Tranças do Rei Careca", 14),
    4: ("Poeira em Alto Mar", 16),
    5: ("A Vingança do Frango Assado", 18)
}

while True:
    print("\n=== FILMES ===")
    print("1 - A Volta dos Que Não Foram (Livre)")
    print("2 - A Roda Quadra (12 anos)")
    print("3 - As Tranças do Rei Careca (14 anos)")
    print("4 - Poeira em Alto Mar (16 anos)")
    print("5 - A Vingança do Frango Assado (18 anos)")

    opcao = int(input("Escolha a sala do filme (1 a 5): "))

    if opcao in filmes:
        filme, classificacao = filmes[opcao]
        if idade >= classificacao:
            with open(f"programa02_02/bilhetes/{nome}.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write("===== BILHETE =====\n")
                arquivo.write(f"Nome: {nome}\n")
                arquivo.write(f"Filme: {filme}\n")
                arquivo.write(f"Classificação: {classificacao if classificacao > 0 else 'Livre'}\n")

            print("\nEntrada permitida!")
            print("Bilhete gerado no arquivo 'bilhete.txt'.")
            break
        else:
            print("\nVocê não tem idade suficiente para esse filme.")
            print("Escolha outro filme.")
    else:
        print("Opção inválida! 😊😛🙈🐶👩‍❤️‍👩👤👩🏾‍🤝‍👩🏻👩🏽‍🤝‍👩🏼🎃👓")
        