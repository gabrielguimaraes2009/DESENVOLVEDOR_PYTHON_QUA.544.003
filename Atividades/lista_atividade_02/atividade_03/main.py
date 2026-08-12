import json

try:
    while True:
        aluno = input('Informe seu nome: ').strip()
        nota1 = float(input('Informe a primeira nota:').replace(',','.'))
        nota2 = float(input('Informe a segunda nota:').replace(',','.'))
        nota3 = float(input('Informe a terceira nota:').replace(',','.'))

        media = (nota1 + nota2 + nota3)/3

        if media >=7 :
            print("Você esta aprovado.")
        else:
            print('Você esta reprovado.')
        
        with open(f"atividade_03/{aluno}.json","w",encoding="utf-8") as f:
             json.dump(aluno, f)


        continuar = input("Deseja inserir outro aluno? ").strip().lower()
        if continuar != "sim":
                break        

except ValueError:
    print("Valor inválido. Por favor, insira um número válido para as notas.")