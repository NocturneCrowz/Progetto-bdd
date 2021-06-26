from tkinter import ttk
import tkinter as tk
import utils
import connection


#Selezionare una riga dalla vista
def OnDoubleClick(event):
    item = tree.focus()

    print("you clicked on", tree.item(item))

    dizionario = tree.item(item, 'values')

    utils.Popup(dizionario)


def Search():
    my_connession.AddEntry()

#Ricerca per nome
def View():
    info = search_field.get()
    tree.delete(*tree.get_children())
    rows = my_connession.View(info)
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)

#Non sono riuscito a far funzionare la stessa funziona per entrambi i casi, ne ho dovute fare due
def Enter(event):
    info = search_field.get()
    tree.delete(*tree.get_children())
    rows = my_connession.View(info)
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)


#Instanzio la classe
my_connession = connection.MyConnector()

#Un sacco di roba ma è tutta UI 
root = tk.Tk()

tk.Label(root, text="Cerca").grid(row=1, column=0, sticky="W", padx=5, ipady=20)

search_field = tk.Entry()
search_field.grid(row=1, column=0, sticky="W", padx=50)
search_field.bind("<Return>", Enter)


tk.Button(text="Display data", command=View).grid(row=1, sticky="W", padx=200)


tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings')

style = ttk.Style(root)
style.configure('my.Treeview', rowheight=30)
tree.configure(style='my.Treeview')


tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="Nome")

tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Descrizione")

tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="DataP")

tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="DataC")

tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="LuogoC")

tree.column("#6", anchor=tk.CENTER)
tree.heading("#6", text="Descrizione")

tree.column("#7", anchor=tk.CENTER)
tree.heading("#7", text="Stato")

tree.column("#8", anchor=tk.CENTER)
tree.heading("#8", text="More info")

tree.grid(row=2, column=0, sticky="WE", padx=10, pady=10)

tree.bind("<Double-1>", OnDoubleClick)

#Per tenere viva la finestra
root.mainloop()

