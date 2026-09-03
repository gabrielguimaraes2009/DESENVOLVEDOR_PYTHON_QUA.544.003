import pyautogui as auto
from datetime import date
from time import sleep

def hoje():
    return date.today().strftime("%d/%m/%Y")


def main():
    auto.PAUSE = 1.0

    auto.press('win')
    auto.write('cmd')
    auto.press('enter')
    auto.write(r"cd C:\Users\ALUNO\GABRIEL GUIMARAES\DESENVOLVEDOR_PYTHON_QUA.544.003")
    auto.press("enter")
    auto.write("git add .")
    auto.press("enter")
    sleep(3)
    auto.write(f'git commit -m "Atualização do dia {hoje()}"')
    auto.press("enter")
    sleep(3)
    auto.write("git push")
    auto.press("enter")
    sleep(7)
    auto.write("exit")
    auto.press("enter")
    auto.alert(text="Finalizado com sucesso!🤖", button="OK")


if __name__ == "__main__":
    main()