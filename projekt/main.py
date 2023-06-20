import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class RandomForestClassifierModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.X = pd.DataFrame
        self.y = None
        self.load_data()

    def load_data(self):
        file_path = "Dry_Bean_Dataset.xlsx"
        if file_path:
            data = pd.read_excel(file_path)
            self.X = data.drop('Class', axis=1)
            self.y = data['Class']
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

    def update_table(self):
        if self.X is not None and self.y is not None:
            for widget in table_frame.winfo_children():
                widget.destroy()
            table = tk.Text(table_frame, height=10, width=50)
            table.insert(tk.END, self.X.to_string(index=False) + '\n\n' + self.y.to_string(index=False))
            table.pack()

    def train_model(self):
        self.load_data()
        self.model.fit(self.X_train, self.y_train)
        self.y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, self.y_pred)
        return accuracy


    def show_confusion_matrix(self):
        if self.X_test is not None and self.y_test is not None:
            self.y_pred = self.model.predict(self.X_test)
            cm = confusion_matrix(self.y_test,  self.y_pred)
            print(cm)
            print(len(self.y))
            fig = plt.figure(figsize=(6, 4))
            ax = fig.add_subplot(111)
            classes = np.unique(self.y)
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=classes, yticklabels=classes, ax=ax)
            ax.set_xlabel('Predicted')
            ax.set_ylabel('Actual')
            ax.set_title(f'Confusion Matrix')
            return fig

    def load_model(self):
        with open('model.pkl', 'rb') as f:
            self.model=pickle.load(f)
        f.close()
    def save_model(self):
        with open('model.pkl', 'wb') as f:
            pickle.dump(self.model, f)
        f.close()

    def show_table(self):
        self.load_data()
        self.y_pred=self.model.predict(self.X_test)
        y = ["real", "Predi"]
        x = []
        for row, i in enumerate(self.y_test):
            print(self.y_pred[row])
            x.append([i, self.y_pred[row]])
        return x, y


    def add_custom_data(self):
        custom_data = simpledialog.askstring('Wprowadź dane', 'Podaj dane oddzielone średnikami')
        if custom_data:
            custom_data = custom_data.replace(',', '.').split(';')
            if len(custom_data)==16:
                print(custom_data)
                data = [float(x.strip()) for x in  custom_data]
                new_data = pd.DataFrame([data], columns=self.X.columns)
                prediction = self.model.predict(new_data)
                messagebox.showinfo('Predykcja', f'Predykcja dla nowych danych: {prediction}')


class GUI:
    def __init__(self, model):
        self.model = model
        self.root = tk.Tk()
        self.root.title("Random Forest Classifier")
        self.create_widgets()

    def create_widgets(self):

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)

        train_button = tk.Button(buttons_frame, text="Ucz model", command=self.train_model)
        train_button.pack(side=tk.LEFT, padx=10)

        cm_button = tk.Button(buttons_frame, text="Pokaż macierz pomyłek", command=self.show_confusion_matrix)
        cm_button.pack(side=tk.LEFT, padx=10)

        table_button = tk.Button(buttons_frame,text="Pokaz tabelke", command=self.show_table)
        table_button.pack(side=tk.LEFT, padx=10)

        load_button = tk.Button(buttons_frame, text="Wczytaj model", command=self.load_model)
        load_button.pack(side=tk.LEFT, padx=10)

        save_button = tk.Button(buttons_frame, text="Zapisz model", command=self.save_model)
        save_button.pack(side=tk.LEFT, padx=10)


        add_data_button = tk.Button(buttons_frame, text="Dodaj własne dane", command=self.add_custom_data)
        add_data_button.pack(side=tk.LEFT, padx=10)

    def train_model(self):
        accuracy = self.model.train_model()
        if accuracy is not None:
            messagebox.showinfo('Dokładność modelu', f"Dokładność modelu: {accuracy:.2f}")
        else:
            messagebox.showerror('Błąd', 'Wczytaj dane przed trenowaniem modelu!')

    def show_confusion_matrix(self):

        fig = self.model.show_confusion_matrix()
        if fig is not None:

            fig_window = tk.Toplevel(self.root)
            fig_window.title("Confusion Matrix")
            canvas = FigureCanvasTkAgg(fig, master=fig_window)
            canvas.draw()
            canvas.get_tk_widget().pack()

    def show_table(self):
        x,y=self.model.show_table()
        fig_window = tk.Toplevel(self.root)
        fig_window.title("Table")
        table = ttk.Treeview(fig_window)
        table['columns'] = y
        for column in y:
            table.heading(column, text=column)
        for row in x:
            table.insert('', tk.END, values=row)
        table.pack()
    def load_model(self):
        self.model.load_model()

    def save_model(self):
        self.model.save_model()

    def add_custom_data(self):
        self.model.add_custom_data()

    def run(self):
        self.root.mainloop()


model = RandomForestClassifierModel()
gui = GUI(model)
gui.run()