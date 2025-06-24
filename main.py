 
import tkinter as tk
from tkinter import ttk
from TestUniversity.run_module import RunModule
from currency_module import CurrencyModule

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Лабораторная статистика")
        self.geometry("800x600")
        tab_control = ttk.Notebook(self)

        tab1 = RunModule(tab_control)
        tab2 = CurrencyModule(tab_control)

        tab_control.add(tab1, text="Пробежки")
        tab_control.add(tab2, text="Курс валют")
        tab_control.pack(expand=1, fill='both')

if __name__ == "__main__":
    app = App()
    app.mainloop()
