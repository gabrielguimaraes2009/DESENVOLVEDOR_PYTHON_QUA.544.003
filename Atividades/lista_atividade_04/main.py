import os
import datetime
from datetime import date

from models import Conta, Pessoa


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def hoje():
    return date.today().strftime("%d/%m/%Y")


def agora():
    return datetime.datetime.now().strftime("%H:%M:%S")


def main():
    limpar()
    nome = input("Informe o nome do titular da conta: ").strip().title()
    cpf = input("Informe o CPF do titular da conta: ").strip()
    titular = Pessoa(nome, cpf)
    cc = Conta(
        titular=titular,
        agencia="1234-5",
        n_conta="10123-4",
        saldo=0.0,
    )
    limpar()
    print(f"Conta criada no dia {hoje()} às {agora()}.")

    while True:
        print("\n0 - Sair do programa")
        print("1 - Consultar dados da conta")
        print("2 - Fazer depósito")
        print("3 - Fazer saque")
        print("4 - Gerar extrato")
        opcao = input("Informe a opção desejada: ").strip()
        limpar()

        match opcao:
            case "0":
                print("Programa encerrado.")
                break
            case "1":
                print(f"Data da consulta: {hoje()}")
                print(f"Hora da consulta: {agora()}")
                cc.consultar_dados()
            case "2":
                try:
                    valor = float(
                        input("Informe o valor a ser depositado: R$ ").replace(",", ".")
                    )
                    if valor > 0:
                        saldo = cc.depositar(valor)
                        print(
                            f"Depósito efetuado com sucesso, "
                            f"às {agora()} do dia {hoje()}."
                        )
                        print(f"Saldo atual: R$ {saldo:.2f}")
                    else:
                        print("O valor do depósito deve ser maior que zero.")
                except ValueError:
                    print("Informe um valor válido.")
            case "3":
                try:
                    valor = float(
                        input("Informe o valor do saque: R$ ").replace(",", ".")
                    )
                    if valor <= 0:
                        print("O valor do saque deve ser maior que zero.")
                    elif valor <= cc.saldo:
                        saldo = cc.sacar(valor)
                        print(
                            f"Saque efetuado com sucesso "
                            f"às {agora()} do dia {hoje()}."
                        )
                        print(f"Saldo atual: R$ {saldo:.2f}")
                    else:
                        print("Saldo insuficiente.")
                except ValueError:
                    print("Informe um valor válido.")
            case "4":
                cc.gerar_extrato()
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()