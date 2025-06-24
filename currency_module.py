import json
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Frame, Label, Button, filedialog

class CurrencyModule(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = Label(self, text="Курс валют")
        self.label.pack()
        self.data = None

        Button(self, text="Загрузить данные", command=self.load_data).pack()
        Button(self, text="Показать график", command=self.plot).pack()
        Button(self, text="Скользящая средняя", command=self.moving_avg).pack()

    def load_data(self):
        path = filedialog.askopenfilename()
        with open(path, 'r') as f:
            self.data = pd.DataFrame(json.load(f))
        print(self.data)

    def plot(self):
        if self.data is not None:
            self.data.plot(x="day", y=["usd", "eur"])
            plt.title("Курс валют")
            plt.show()

    def moving_avg(self):
        if self.data is not None:
            n = 3
            usd_forecast = self.data["usd"].rolling(window=n).mean()
            eur_forecast = self.data["eur"].rolling(window=n).mean()
            plt.plot(self.data["day"], self.data["usd"], label="USD")
            plt.plot(self.data["day"], usd_forecast, label="USD прогноз", color="red")
            plt.plot(self.data["day"], self.data["eur"], label="EUR")
            plt.plot(self.data["day"], eur_forecast, label="EUR прогноз", color="green")
            plt.legend()
            plt.title("Прогноз по курсам валют")
            plt.show()
