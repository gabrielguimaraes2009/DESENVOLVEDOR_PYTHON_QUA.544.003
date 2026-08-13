import os
import json

alunos = []

os.system("cls" if os.name == "nt" else "clear ")

try:
    while True:
        nome = input('Informe o nome do aluno:').strip().title()
        
        notas = [0,0,0]
        nota1 = float(input('Informe a primeira nota:').replace(',','.'))
        nota2 = float(input('Informe a segunda nota:').replace(',','.'))
        nota3 = float(input('Informe a terceira nota:').replace(',','.'))

        media = (nota1 + nota2 + nota3)/3

        if media >= 7:
            situacao = "Aprovado"
            print("Você está aprovado.")
        else:
            situacao = "Reprovado"
            print("Você está reprovado.")

        aluno = {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3,
            "media": media,
            "situacao": situacao
        }

        alunos.append(aluno)

        # Gravar no arquivo JSON
        with open("alunos.json", "w", encoding="utf-8") as arquivo:
            json.dump(alunos, arquivo, ensure_ascii=False, indent=4)

        continuar = input("Deseja inserir outro aluno? ").strip().lower()
        if continuar != "sim":
                break        

except ValueError:
    print("Valor inválido. Por favor, insira um número válido para as notas.")