from tkinter import *
from tkinter import ttk
from async_tkinter_loop import async_mainloop
import asyncio

root = Tk()
root.title("AutoClick")
root.geometry("450x400")

# Атрибуты окна
root.resizable(False, False)
root.attributes("-alpha", 0.7)

# Кнопки
btn = ttk.Button(text="Button")
btn.pack()


async_mainloop(root)
