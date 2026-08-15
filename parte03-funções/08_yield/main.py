from modulo import limpar, equacao_segundo_grau

def main():
    limpar()

    a = int(input("Informe o valor de A: "))
    b = int(input("Informe o valor de B: "))
    c = int(input("Informe o valor de C: "))
    limpar()

    result = equacao_segundo_grau(a, b, c)
    print("Resolução da equação do 2° grau:")
    for x in result:
        print(f"x = {x}")

if __name__ == "__main__":
        main()