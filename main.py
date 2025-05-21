from tkinter import *
from tkinter import ttk
import keyboard
import pyautogui
import threading
import time

pyautogui.FAILSAFE = True

# Создание окна
root = Tk()
root.title('AutoClick')
root.geometry('350x250')
root.resizable(False, False)
root.attributes('-alpha', 0.7)
root.attributes('-topmost', True)

# Переменные
click_active = False


# Функция кликера в потоке
def autoclick_worker():
    while click_active:
        pyautogui.tripleClick()
        time.sleep(0.01)  # Задержка 10 мс (для примера)


# Запуск/остановка кликера
def start_click():
    global click_active
    if not click_active:
        click_active = True
        thread = threading.Thread(target=autoclick_worker, daemon=True)
        thread.start()


def stop_click():
    global click_active
    click_active = False


# Назначение горячих клавиш
keyboard.add_hotkey('f5', start_click)
keyboard.add_hotkey('f6', stop_click)

# Интерфейс
input_click = ttk.Entry()
input_click.place(x=95, y=45, height=20, width=160)
input_click.insert(0, "10")  # Значение по умолчанию

ttk.Label(text='Задержка (мс):').place(x=120, y=20)

# Надписи над кнопками
ttk.Label(text="Start (F5)").place(x=211, y=150)
ttk.Label(text="Stop (F6)").place(x=81, y=150)

# Кнопки
btn1 = ttk.Button(text='Start', command=start_click)
btn1.place(x=195, y=170, height=45, width=90)
btn2 = ttk.Button(text='Stop', command=stop_click)
btn2.place(x=65, y=170, height=45, width=90)

root.mainloop()
