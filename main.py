from tkinter import *
from tkinter import ttk
import pyautogui
from async_tkinter_loop import async_mainloop

pyautogui.FAILSAFE = True

# Создание окна
root = Tk()
root.title("AutoClick")
root.geometry('350x250')

# Атрибуты окна
root.resizable(False, False)
root.attributes("-alpha", 0.7)
root.attributes('-topmost', True)


# AutoClicker
def hello():
    label = ttk.Label(text=f'Выбрано:{input_click.get()} cps')
    label.place(x=120, y=20)


# Кнопки
btn1 = ttk.Button(text='Start', command=hello)
btn1.place(x=65, y=170, height=45, width=90)
btn2 = ttk.Button(text='Stop', command=hello)
btn2.place(x=195, y=170, height=45, width=90)

input_click = ttk.Entry()
input_click.place(x=95, y=45, height=20, width=160)

async_mainloop(root)
