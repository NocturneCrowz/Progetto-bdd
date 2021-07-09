from tkinter import ttk
import tkinter as tk
import utils
import connection


#Selezionare una riga dalla vista
def OnDoubleClick(event):
    item = tree.focus()
    dizionario = tree.item(item, 'values')
    utils.Popup(dizionario)
    

#Ricerca per nome
def View():
    my_connession = connection.MyConnector()
    info = search_field.get()
    tree.delete(*tree.get_children())
    rows = my_connession.View(info)
    for row in rows:
        if row[0] != "---":
            tree.insert("", tk.END, values=row)
        

#Non sono riuscito a far funzionare la stessa funzione per entrambi i casi, ne ho dovute fare due
def Enter(event):
    my_connession = connection.MyConnector()
    info = search_field.get()
    tree.delete(*tree.get_children())
    rows = my_connession.View(info)
    for row in rows:
        if row[0] != "---":
            tree.insert("", tk.END, values=row)
        
#Inserimento di un record nel database, gestito da utils.py
def Insertion():
    utils.Insert()
    



#UI per la visualizzazione dei dati principali dei campioni
root = tk.Tk()
root.title("Database View")

tk.Label(root, text="Cerca").grid(row=1, column=0, sticky="W", padx=5, ipady=20)

search_field = tk.Entry()
search_field.grid(row=1, column=0, sticky="W", padx=50)
search_field.bind("<Return>", Enter)


tk.Button(text="Cerca", command=View).grid(row=1, sticky="W", padx=200)

tk.Button(text="Aggiungi un record", command=Insertion).grid(row=1, sticky="W", padx=500)

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')

style = ttk.Style(root)
style.configure('my.Treeview', rowheight=30)
tree.configure(style='my.Treeview')


tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="Nome")

tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Data Prelievo")

tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Data Catalogazione")

tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="Luogo Catalogazione")

tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="Stato")

tree.column("#6", anchor=tk.CENTER)
tree.heading("#6", text="Descrizione")

tree.grid(row=2, column=0, sticky="WE", padx=10, pady=10)

tree.bind("<Double-1>", OnDoubleClick)


if __name__ == '__main__': 
    #Per tenere viva la finestra
    root.mainloop()

