class Pessoa:
    def __init__(self, nome, idade, email, altura):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.altura = altura
    def exibir_dados(self):
        print(f"E-mail: {self.email}")
        print(f"Altura: {self.altura} metros")

def main():
    # instancia a classe (cria o objeto)
    usuario = Pessoa(nome="",idade=0,email="",altura=0.0)

    usuario.nome = input("Digite o nome: ").strip().title()
    usuario.idade = int(input("Digite a idade: "))
    usuario.email = input("Digite o e-mail: ").strip().lower()
    usuario.altura = float(input("Digite a altura em metros: ").replace(",","."))

    usuario.exibir_dados()


if __name__ == "__main__":
    main()