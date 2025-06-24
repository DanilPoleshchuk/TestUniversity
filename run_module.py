import json
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Frame, Label, Button, filedialog, Text

class RunModule(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = Label(self, text="Пробежки")
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
            self.data.plot(x="day", y=["distance_km", "avg_heart_rate"])
            plt.title("График пробежек")
            plt.show()

    def moving_avg(self):
        if self.data is not None:
            n = 5
            forecast = self.data["distance_km"].rolling(window=n).mean()
            plt.plot(self.data["day"], self.data["distance_km"], label="Факт")
            plt.plot(self.data["day"], forecast, label="Прогноз", color="red")
            plt.legend()
            plt.title("Прогноз пробежек по скользящей средней")
            plt.show()
