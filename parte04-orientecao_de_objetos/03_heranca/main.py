import os

from models import PessoaFisica, PessoaJuridica

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    usuario = PessoaFisica(nome="", telefone="", endereco="", cpf="", email="")
    empresa = PessoaJuridica(razao_social="", nome_fantasia="", email="", cnpj="", telefone="", endereco="")

    # informa os valores do usuario
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.endereco = input("Informe o endereço: ")
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.email = input("Informe o email: ").strip().lower()

    limpar()

    # informa os dados da empresa
    empresa.razao_social = input("Informe o nome juridico da empresa: ").strip()
    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip()
    empresa.email = input("Informe o email da empresa: ").strip().lower()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ")

    # saída de dados
    usuario.exibir_dados()
    empresa.exibir_dados()

if __name__ == "__main__":
    main()