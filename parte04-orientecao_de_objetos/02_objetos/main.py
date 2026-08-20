import os

from models import Pessoa

def Limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    Limpar()
    # instancia a classe (cria o objeto)

    homem = Pessoa(nome="",idade=0,email="",telefone="")
    mulher = Pessoa(nome="",idade=0,email="",telefone="")

    # informa os dados do homem
    homem.nome = input("Informe o nome do homem: ").strip().title()
    homem.idade = int(input("Informe a idade do homem: "))
    homem.email = input("Informe o e-mail do homem: ").strip().lower()
    homem.telefone = input("Informe o telefone do homem: ").strip()

    # informa os dados da mulher
    mulher.nome = input("Informe o nome da mulher: ").strip().title()
    mulher.idade = int(input("Informe a idade da mulher: "))
    mulher.email = input("Informe o e-mail da mulher: ").strip().lower()   
    mulher.telefone = input("Informe o telefone da mulher: ").strip()

    # execuçaõ dos métodos
    print(homem.apresentar())
    print(homem.cumprimentar(mulher.nome))
    print(mulher.cumprimentar(homem.nome))


if __name__ == "__main__":
    main() 