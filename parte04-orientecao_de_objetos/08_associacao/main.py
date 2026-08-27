from models import Endereco, Pessoa



def main():
    endereco = Endereco(uf="",cidade="")
    usuario = Pessoa(nome="",endereco=endereco)

    usuario.nome = input("Informe o nome do usuário: ").strip()
    usuario.endereco.uf = input("Informe o estado: ").strip()
    endereco.uf = input("Informe o estado: ").strip()

    usuario.apresentar_endereco()

if __name__ == '__main__':
    main()