from tkinter import *
from tkinter import ttk
import ctypes
import sys
import keyboard
import pyautogui
import threading
import time

# Проверка прав администратора (для работы keyboard)
if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, ' '.join(sys.argv), None, 1)
    sys.exit()

pyautogui.FAILSAFE = True

# Создание окна
root = Tk()
root.title('AutoClick (CPS Control)')
root.geometry('350x250')
root.resizable(False, False)
root.attributes('-alpha', 0.7)
root.attributes('-topmost', True)

# Переменные
click_active = False

def autoclick_worker():
    while click_active:
        try:
            cps = float(cps_entry.get())
            if cps <= 0:
                cps = 1
            interval = 1.0 / cps
        except:
            interval = 0.1

        pyautogui.click()
        time.sleep(interval)

def start_click():
    global click_active
    if not click_active:
        click_active = True
        thread = threading.Thread(target=autoclick_worker, daemon=True)
        thread.start()

def stop_click():
    global click_active
    click_active = False

# Горячие клавиши
keyboard.add_hotkey('f5', start_click)
keyboard.add_hotkey('f6', stop_click)

# Интерфейс
cps_entry = ttk.Entry()
cps_entry.place(x=95, y=45, height=20, width=160)
cps_entry.insert(0, '10')

ttk.Label(text='Кликов в секунду (CPS):').place(x=100, y=20)

# Надписи над кнопками
ttk.Label(text='Start (F5)').place(x=211, y=150)
ttk.Label(text='Stop (F6)').place(x=81, y=150)

# Кнопки
btn1 = ttk.Button(text='Start', command=start_click)
btn1.place(x=195, y=170, height=45, width=90)
btn2 = ttk.Button(text='Stop', command=stop_click)
btn2.place(x=65, y=170, height=45, width=90)

root.mainloop()
