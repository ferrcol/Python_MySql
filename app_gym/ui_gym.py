import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

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
        self.show_buttons()

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
        label.grid(row=0, column=0, columnspan=3, pady=30)

    def show_form(self):
        self.frame_form = ttk.Frame()

        #first name
        first_name_label = ttk.Label(self.frame_form, text="First Name: ")
        first_name_label.grid(row=0, column=0, sticky=tk.W, pady = 30, padx=5)
        self.first_name_t = ttk.Entry(self.frame_form)
        self.first_name_t.grid(row=0, column=1)

        #Last name
        last_name_label = ttk.Label(self.frame_form, text="Last Name: ")
        last_name_label.grid(row=1, column=0, sticky=tk.W, pady = 30, padx=5)
        self.last_name_t = ttk.Entry(self.frame_form)
        self.last_name_t.grid(row=1, column=1)

        #Mambership
        membership_label = ttk.Label(self.frame_form, text="Mambership ")
        membership_label.grid(row=2, column=0, sticky=tk.W, pady = 30, padx=5)
        self.membership_t = ttk.Entry(self.frame_form)
        self.membership_t.grid(row=2, column=1)

        self.frame_form.grid(row=1, column=0)

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

    def show_buttons(self):
        self.frame_buttons = ttk.Frame()

        add_button = ttk.Button(self.frame_buttons, text="Save", command=self.validate_costumer)
        add_button.grid(row=0,column=0,padx=30)

        delete_button = ttk.Button(self.frame_buttons, text="Delete", command=self.delete_costumer)
        delete_button.grid(row=0,column=1,padx=30)
        
        clean_button = ttk.Button(self.frame_buttons, text="Clean", command=self.clean_fields)
        clean_button.grid(row=0,column=2,padx=30)

        self.styles.configure("TButton", background = "#005f73")
        self.styles.map("TButton", background = [("active", "#0a9396")])

        self.frame_buttons.grid(row=2,column=0, columnspan=3, pady=20)

    def validate_costumer(self):
        if(self.first_name_t.get() and self.last_name_t.get() and self.membership_t.get()):
            if self.num_membership():
                self.save_costumer()
            else:
                showerror(title="Attention", message= "Membership should be a valid number")
                self.membership_t.delete(0, tk.END)
                
        else:
            showerror(title="Attention", message= "All the values need to be complete")
            self.first_name_t.focus_set()

        

    def num_membership(self):
        try:
            int(self.membership_t.get())
            return True
        except:
            return False

    def save_costumer(self):
        pass

    def delete_costumer(self):
        pass

    def clean_fields(self):
        pass




if __name__ == "__main__":
    app = App()
    app.mainloop()

        