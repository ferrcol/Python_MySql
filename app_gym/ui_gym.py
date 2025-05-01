import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    WINDOWS_COLOR = "#1a1c40"

    def __init__(self):
        super().__init__()
        self.windows_config()

    def windows_config(self):
        self.geometry("900x600")
        self.title("App Gym")
        self.configure(background=App.WINDOWS_COLOR)

        self.styles = ttk.Style()
        self.styles.theme_use("clam")
        self.styles.configure(self, background=App.WINDOWS_COLOR, foreground="white", fieldbackground="black")

if __name__ == "__main__":
    app = App()
    app.mainloop()
        