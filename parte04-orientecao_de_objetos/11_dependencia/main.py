from models import Pedido

import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

    def main():
        pedido = Pedido(valor1=10, valor2=0)

        limpar()

        pedido.valor1 = float(input("Informe o primeiro valor: ").replace(",","."))
        pedido.valor2 = float(input("Informe o segundo valor: ").replace(",","."))

        limpar()

        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        operador = input("Informe a operação desejada: ").strip()
        print(pedido.calcular_total (operador=operador))



    if __name__ == "__main__":
        main()