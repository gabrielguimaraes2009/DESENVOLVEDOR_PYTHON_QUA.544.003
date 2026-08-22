import os

from models import Pessoa

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar()

    usuario = Pessoa(nome="", cpf="", email="", telelfone="")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.email = input("Informe o email: ").strip().lower()
    usuario.telefone = input("Informe o telefone: ").strip()

    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Email: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")

if __name__ == "__main__":
        main()