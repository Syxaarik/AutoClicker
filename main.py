from tkinter import *
from tkinter import ttk
import pyautogui
from async_tkinter_loop import async_mainloop

pyautogui.FAILSAFE = True
click = True

# Создание окна
root = Tk()
root.title("AutoClick")
root.geometry('350x250')

# Атрибуты окна
root.resizable(False, False)
root.attributes("-alpha", 0.7)
root.attributes('-topmost', True)


# AutoClicker
def start_click():
    global click
    click_timer = input_click.get()
    click = True

    if click:
        while click:
            pyautogui.click()
            root.update()
    else:
        click = True
    root.update()


def stop_click():
    global click
    click = False
    root.update()


# Кнопки
btn1 = ttk.Button(text='Start', command=start_click)
btn1.place(x=195, y=170, height=45, width=90)
btn2 = ttk.Button(text='Stop', command=stop_click)
btn2.place(x=65, y=170, height=45, width=90)

input_click = ttk.Entry()
input_click.place(x=95, y=45, height=20, width=160)

label = ttk.Label()
label.place(x=120, y=20)

async_mainloop(root)
