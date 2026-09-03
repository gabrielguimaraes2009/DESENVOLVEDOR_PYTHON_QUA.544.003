import pyautogui as auto
from time import sleep

def ir_pesquisa():
    auto.press("tab")
    auto.press("tab")
    auto.press("tab")
    auto.press("tab")

def main():
    auto.PAUSE = 0.75
    auto.press("win")
    auto.write("firefox")
    auto.press("enter")
    auto.write("youtube.com.br")
    auto.press("enter")
    sleep(5)
    ir_pesquisa()
    auto.write("python")
    auto.press("enter")
    sleep(5)
    auto.hotkey("ctrl", "f4")

if __name__ == "__main__":
    main()