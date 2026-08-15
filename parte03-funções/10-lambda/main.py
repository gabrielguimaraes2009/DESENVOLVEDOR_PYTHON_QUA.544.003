somar = lambda x,y: x+y

def main():
    x = int(input("Informe o valor de X: "))
    y = int(input("Informe o valor de Y: "))
    print(f"A soma de {x} + {y} é {somar(x,y)}")

if __name__ == "__main__":
    main()