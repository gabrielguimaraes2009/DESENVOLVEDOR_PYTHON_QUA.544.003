import pyautogui as auto
from datetime import date
from time import sleep

def hoje():
    return date.today().strftime("%d/%m/%Y")


def main():
    auto.PAUSE = 1.3

    auto.press('win')
    auto.write('cmd')
    auto.press('enter')
    auto.write(r"cd C:\Users\ALUNO\GABRIEL GUIMARAES\DESENVOLVEDOR_PYTHON_QUA.544.003")
    auto.press("enter")
    auto.write("git add .")
    sleep(3)
    auto.press("enter")
    auto.write(f'git commit -m "Atualização do dia {hoje()}"')
    auto.press("enter")
    auto.write("git push")
    sleep(7)
    auto.press("enter")
    auto.write("exit"),


if __name__ == "__main__":
    main()