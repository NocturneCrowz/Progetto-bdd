import tkinter as tk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

#Classe per connettermi al DB
class MyConnector():

    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', database='progettobdd', user='root', password='@774c3n2')
        self.Setup()

    #Setup iniziale con debug da terminale
    def Setup(self):

        if self.connection.is_connected():
            db_Info = self.connection.get_server_info()

            print("Connected to MySQL Server version ", db_Info)

            cursor = self.connection.cursor()

            cursor.execute("select database();")

            record = cursor.fetchone()

            print("You're connected to database: ", record)

            cursor = self.connection.cursor()

            self.connection.commit()

            cursor.close()

    #Ricerca per nome del campione, ritorna una lista
    def View(self, search_value):

        cursor = self.connection.cursor()

        if search_value == "":
            cursor.execute("""select campione.Nome, campione.Descrizione, stato.Nome as Stato, opera.Nome as Opera, autore.Nome as Autore 
                            from campione JOIN stato on campione.IdStato = stato.IdStato JOIN opera on campione.IdOpera = opera.IdOpera JOIN autore on opera.IdAutore = autore.IdAutore""")

        else:

            cursor.execute("""select campione.Nome, campione.Descrizione, stato.Nome as Stato, opera.Nome as Opera, autore.Nome as Autore 
                        from campione JOIN stato on campione.IdStato = stato.IdStato JOIN opera on campione.IdOpera = opera.IdOpera JOIN autore on opera.IdAutore = autore.IdAutore
                        where campione.Nome = (%s)""", (search_value,))

        rows = cursor.fetchall()    
      
        cursor.close()

        return rows

    #TODO 
    def AddEntry(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("insert into autore(Nome) values ('Leonardo Da Vinci')")

        except Error as e:
            popup = tk.Toplevel()
            tk.Label(popup, text="Error").grid(row=0,column=0)
            ttk.Button(popup, text="Close", command=popup.destroy).grid_anchor('n')
            
            #b.grid(row=1, sticky="S", padx = 10, pady = 10)
            print(e)
        finally:
            cursor.close()
