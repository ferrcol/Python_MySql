import tkinter as tk
from tkinter import ttk

from costumer_dao import CostumerDAO


class App(tk.Tk):
    WINDOWS_COLOR = "#1a1c44"

    def __init__(self):
        super().__init__()
        self.windows_config()
        self.grid_config()
        self.show_title()
        self.show_form()
        self.show_table()

    def windows_config(self):
        self.geometry("900x600")
        self.title("App Gym")
        self.configure(background=App.WINDOWS_COLOR)

        self.styles = ttk.Style()
        self.styles.theme_use("clam")
        self.styles.configure(self, background=App.WINDOWS_COLOR, foreground="white", fieldbackground="black")

    def grid_config(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def show_title(self):
        label = ttk.Label(self, text="Users Gym Manager", font=("Times New Roman", 25), background=App.WINDOWS_COLOR, foreground="white")
        label.grid(row=0, column=0, columnspan=2, pady=20)

    def show_form(self):
        pass

    def show_table(self):
        self.frame_table = ttk.Frame(self)
        self.styles.configure("Treeview", background="black", foreground="white", filedbackground="black", rowheight=20)
        columns = ("Id","First Name", "Last Name", "Membership")
        self.table = ttk.Treeview(self.frame_table, columns=columns, show="headings")

        self.table.heading("Id", text="Id", anchor=tk.CENTER)
        self.table.heading("First Name", text="First Name", anchor=tk.W)
        self.table.heading("Last Name", text="Last Name", anchor=tk.W)
        self.table.heading("Membership", text="Membarship", anchor=tk.W)

        self.table.column("Id", anchor=tk.CENTER, width=50)
        self.table.column("First Name", anchor=tk.W, width=150)
        self.table.column("Last Name", anchor=tk.W, width=150)
        self.table.column("Membership", anchor=tk.W, width=50)

        costumers = CostumerDAO.select()
        for costumer in costumers:
            self.table.insert(parent="", index=tk.END, values=(costumer.id, costumer.first_name, costumer.last_name, costumer.membership))

        scrollbar = ttk.Scrollbar(self.frame_table, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll = scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        self.table.grid(row=0,column=0)

        self.frame_table.grid(row=1,column=2, padx=20)



if __name__ == "__main__":
    app = App()
    app.mainloop()

        