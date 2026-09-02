from deep_translator import GoogleTranslator
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def traduzir(texto):
    rtadutor = GoogleTranslator(source='auto', target='pt')
    return rtadutor.translate(texto)

def menu():
    print("=== Tradutor ===")
    print("1. Traduzir texto")
    print("2. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def main():
    limpar()
    while True:
        opcao = menu()
        if opcao == "2":
            break
        elif opcao == "1":
            try:
                texto = input("Informe o texto a ser traduzido: ")
                limpar()
                texto_traduzido = traduzir(texto)
                print(texto_traduzido)
            except Exception as e:
                print(f"Erro ao traduzir: {e}")
            continue
        else:
            print("Opção inválida.")
            continue

if __name__ == "__main__":
    main()