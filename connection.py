import tkinter as tk
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

    #Ricerca per nome del campione, ritorna una lista di liste (solo 1 lista in caso di un singolo record)
    def View(self, search_value):

        cursor = self.connection.cursor()

        if search_value == "":
            cursor.execute("""SELECT campione.Nome, campione.DataP, campione.DataC, campione.LuogoC, stato.Nome as Stato, campione.Descrizione, campione.IdOpera, ifnull(campione.IdLaboratorio, 1), campione.IdCampione 
                                FROM campione JOIN stato ON campione.IdStato = stato.IdStato""")

        else:

            cursor.execute("""SELECT campione.Nome, campione.DataP, campione.DataC, campione.LuogoC, stato.Nome as Stato, campione.Descrizione, campione.IdOpera, ifnull(campione.IdLaboratorio, 1), campione.IdCampione 
                                FROM campione JOIN stato ON campione.IdStato = stato.IdStato 
                                WHERE campione.Nome = (%s)""", (search_value,))

        rows = cursor.fetchall()    
      
        cursor.close()

        return rows

    #Aggiunge una entry al DB
    def AddEntry(self, query_list):
        try:
            cursor = self.connection.cursor(buffered = True)

            cursor.execute("""SELECT MAX(IdRelatore) FROM relatore """)
            id_row_relatore = cursor.fetchone()

            if id_row_relatore[0] == None:
                id_relatore = 1
            else:
                id_relatore = id_row_relatore[0] + 1

            cursor.execute("""INSERT INTO relatore (IdRelatore, Nome, Afferenza) 
                              SELECT %s, %s, %s 
                              WHERE NOT EXISTS 
                                (SELECT Nome, Afferenza FROM relatore WHERE Nome= (%s) AND Afferenza = (%s))""", (id_relatore, query_list[19], query_list[20], query_list[19], query_list[20]))

            cursor.execute("""SELECT IdRelatore FROM relatore WHERE Nome= (%s) AND Afferenza = (%s)""", (query_list[19], query_list[20]))
            id_row_relatore = cursor.fetchone() 

            cursor.execute("""SELECT MAX(IdArticolo) FROM Articolo """)
            id_row_articolo = cursor.fetchone()

            if id_row_articolo[0] == None:
                id_articolo = 1
            else:
                id_articolo = id_row_articolo[0] + 1

            cursor.execute("""INSERT INTO articolo (IdArticolo, Articolo, NomePubblicatore, Data, Link) 
                              SELECT %s, %s, %s, %s, %s 
                              WHERE NOT EXISTS 
                                (SELECT Articolo, NomePubblicatore FROM articolo WHERE Articolo = (%s) AND NomePubblicatore = (%s))""", (id_articolo, query_list[15], query_list[16], query_list[17], query_list[18], query_list[15], query_list[16]))

            cursor.execute("""SELECT IdArticolo FROM articolo WHERE Articolo= (%s)""", (query_list[15],))
            id_row_articolo = cursor.fetchone()              

            cursor.execute("""INSERT INTO scritto (IdArticolo, IdRelatore)
                               SELECT %s, %s
                               WHERE NOT EXISTS 
                                (SELECT IdArticolo, IdRelatore FROM scritto WHERE IdArticolo = (%s) AND IdRelatore = (%s))""", (id_row_articolo[0], id_row_relatore[0], id_row_articolo[0], id_row_relatore[0]))


            cursor.execute("""INSERT INTO laboratorio(Nome, DataInvio)
                                VALUES (%s, %s) """, (query_list[13], query_list[14]))
            cursor.execute("""SELECT IdLaboratorio FROM laboratorio WHERE Nome = (%s) AND DataInvio = (%s) """, (query_list[13], query_list[14]))
            id_lab = cursor.fetchone()
            


            cursor.execute("""INSERT INTO provenienza (Nome, Comune, Provincia) 
                              SELECT %s, %s, %s 
                              WHERE NOT EXISTS 
                                (SELECT Nome, Comune FROM provenienza WHERE Nome = (%s) AND Comune = (%s));""", (query_list[10], query_list[11], query_list[12], query_list[10], query_list[11]))

            cursor.execute("""SELECT IdProvenienza FROM provenienza WHERE Nome = (%s) AND Comune = (%s)""", (query_list[10], query_list[11]))
            id_provenienza = cursor.fetchone() 


            cursor.execute("""INSERT INTO autore (Nome) 
                              SELECT %s 
                              WHERE NOT EXISTS 
                                (SELECT Nome FROM autore WHERE Nome= (%s)) """, (query_list[9], query_list[9]))

            cursor.execute("""SELECT IdAutore FROM autore WHERE Nome = (%s) """, (query_list[9],))
            id_autore = cursor.fetchone()


            cursor.execute("""INSERT INTO opera (Nome, Periodo, Tipologia, IdAutore, IdProvenienza) 
                              SELECT %s, %s, %s, %s, %s 
                              WHERE NOT EXISTS 
                                (SELECT Nome, IdAutore FROM opera WHERE Nome = (%s) AND IdAutore = (%s) AND IdProvenienza = (%s));""", (query_list[6], query_list[7], query_list[8], id_autore[0], id_provenienza[0], query_list[6], id_autore[0], id_provenienza[0]))

            cursor.execute("""SELECT IdOpera FROM opera WHERE Nome = (%s) AND IdAutore = (%s) AND IdProvenienza = (%s)""", (query_list[6], id_autore[0], id_provenienza[0]))
            id_opera = cursor.fetchone()


            cursor.execute("""INSERT INTO stato (Nome)
                              SELECT %s
                              WHERE NOT EXISTS
                                (SELECT Nome FROM stato WHERE Nome = (%s)) """, (query_list[4], query_list[4]))

            cursor.execute("""SELECT IdStato FROM stato WHERE Nome = (%s) """, (query_list[4], ))
            id_stato = cursor.fetchone()

            
            cursor.execute("""INSERT INTO campione (Nome, DataP, DataC, LuogoC, Descrizione, IdOpera, IdLaboratorio, IdStato) 
                              SELECT %s, %s, %s, %s, %s, %s, %s, %s
                              WHERE NOT EXISTS 
                                (SELECT * FROM campione WHERE Nome = (%s) AND IdOpera = (%s))""", (query_list[0], query_list[1], query_list[2], query_list[3], query_list[5], id_opera[0], id_lab[0], id_stato[0], query_list[0], id_opera[0]))

            cursor.execute("""SELECT IdCampione FROM campione WHERE Nome = (%s) AND IdOpera = (%s)""", (query_list[0], id_opera[0]))
            id_campione = cursor.fetchone()

    
            cursor.execute("""INSERT INTO citato (IdCampione, IdArticolo)
                              SELECT %s, %s
                              WHERE NOT EXISTS 
                                (SELECT * FROM citato WHERE IdCampione = (%s) AND IdArticolo = (%s))""", (id_campione[0], id_row_articolo[0], id_campione[0], id_row_articolo[0]))


            self.connection.commit()

        except Error as e:
            popup = tk.Toplevel()
            tk.Label(popup, text="Error." + str(e)).grid(row=0,column=0, ipady = 20)
            tk.Label(popup, text="").grid(row=1,column=0, ipady = 10)
            tk.Button(popup, text="Close", command=popup.destroy).grid(row=2, column=0, pady=10)
            
        finally:
            cursor.close()

    #Cancella il campione con ID = id 
    def DeleteEntry(self, id):
        cursor = self.connection.cursor()
        
        try:
            cursor.execute("""DELETE FROM campione WHERE IdCampione = (%s)""", (id,))
            self.connection.commit()

        except Error as e:
            popup = tk.Toplevel()
            tk.Label(popup, text="Error. "+ str(e)).grid(row=0,column=0, ipady = 20)
            tk.Label(popup, text="").grid(row=1,column=0, ipady = 10)
            tk.Button(popup, text="Close", command=popup.destroy).grid(row=2, column=0, pady=10)

        finally:
            cursor.close()

        
    #Restituisce le info di vari record
    def GetRecord(self, search, id=0):

        cursor = self.connection.cursor()

        def Opera(id):
            if id == 0:
                cursor.execute("""SELECT * FROM opera JOIN autore ON opera.IdAutore = autore.IdAutore""")
            else:
                cursor.execute("""SELECT * FROM opera JOIN autore ON opera.IdAutore = autore.IdAutore WHERE opera.IdOpera = (%s)""", (id,))

        def Laboratorio(id):
            cursor.execute("""SELECT * FROM laboratorio WHERE laboratorio.IdLaboratorio = (%s)""", (id,))

        def Provenienza(id):
            cursor.execute("""SELECT * FROM provenienza WHERE provenienza.IdProvenienza = (%s)""", (id,))

        def Citato(id):
            cursor.execute("""SELECT * FROM citato WHERE citato.IdCampione = (%s) """, (id,))

        def Articolo(id):
            cursor.execute("""SELECT * FROM articolo WHERE articolo.IdArticolo = (%s) """, (id,))

        def Scritto(id):
            cursor.execute("""SELECT * FROM scritto WHERE scritto.IdArticolo = (%s) """, (id,))
        
        def Relatore(id):
            cursor.execute("""SELECT * FROM relatore WHERE relatore.IdRelatore = (%s) """, (id,))


        switcher = {
            1: Opera,
            2: Scritto,
            3: Laboratorio,
            4: Provenienza,
            5: Citato,
            6: Articolo,
            7: Relatore
        }
        
        choice = switcher.get(search)
        choice(id)

        rows = cursor.fetchall()    
      
        cursor.close()

        return rows

