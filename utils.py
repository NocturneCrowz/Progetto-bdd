import tkinter as tk
from tkinter import scrolledtext
from datetime import date
import connection

frame_counter = 0

#UI del popup per maggiori info
def Popup(item):

    def Delete():

        def DeleteEntry():
            my_connession.DeleteEntry(item[8])
            popup1.destroy()
            popup.destroy()
            

        popup1 = tk.Toplevel()
        popup1.title("Cancella")
        tk.Label(popup1, text="Sei sicuro? Il procedimento non può essere invertito.").pack(pady = 20)
        tk.Button(popup1, text="Si", command=DeleteEntry).pack(side='left', ipadx=20, pady=10, padx=20)
        tk.Button(popup1, text="No", command=popup1.destroy).pack(side='right', ipadx=20, pady=10, padx=20)


    popup = tk.Toplevel()
    popup.geometry("450x650")
    popup.title("Dettagli")

    my_connession = connection.MyConnector()

    temp = []
    for record in my_connession.GetRecord(1, item[6]):
        temp.append(record)
    info_opera = temp[0]

    temp1 = []
    for record in my_connession.GetRecord(4, info_opera[5]):
        temp1.append(record)
    info_provenienza = temp1[0]

    temp2 = []
    for record in my_connession.GetRecord(3, item[7]):
        temp2.append(record)
    info_laboratorio = temp2[0]

    temp3 = []
    for record in my_connession.GetRecord(5, item[8]):
        temp3.append(record[1])

    info_citazioni = []
    for record in temp3:
        info_citazioni.append(my_connession.GetRecord(6, record))
    

    text_area = scrolledtext.ScrolledText(popup, spacing3 = 2, wrap = tk.WORD, width = 440, height = 640, font = ("Courier", 10))
    tk.Button(popup, text="Delete Entry", command=Delete).pack(anchor='w', padx=30, pady=10)
    text_area.pack(fill='both')
    
    text_area.focus()

    text_area.insert('end', "---- Campione ----"+'\n\n', "campione")
    text_area.insert('end', "Nome"+'\n', "nomeC")
    text_area.insert('end', item[0]+'\n')
    text_area.insert('end', "Data Prelievo"+'\n', "dataP")
    text_area.insert('end', item[1]+'\n')
    text_area.insert('end', "Data Catalogazione"+'\n', "dataC")
    text_area.insert('end', item[2]+'\n')
    text_area.insert('end', "Luogo Catalogazione"+'\n', "luogoC")
    text_area.insert('end', item[3]+'\n')
    text_area.insert('end', "Stato"+'\n', "stato")
    text_area.insert('end', item[4]+'\n')
    text_area.insert('end', "Descrizione"+'\n', "descrizione")
    text_area.insert('end', item[5]+'\n')

    text_area.insert('end', '\n'+"---- Opera ----"+'\n\n', "opera")
    text_area.insert('end', "Opera"+'\n', "nomeO")
    text_area.insert('end', info_opera[1]+'\n')
    text_area.insert('end', "Periodo"+'\n', "periodo")
    text_area.insert('end', info_opera[2]+'\n')
    text_area.insert('end', "Tipologia"+'\n', "tipologia")
    text_area.insert('end', info_opera[3]+'\n')

    text_area.insert('end', '\n'+"---- Provenienza ----"+'\n\n', "provenienza")
    text_area.insert('end', "Nome"+'\n', "nomeP")
    text_area.insert('end', info_provenienza[1]+'\n')
    text_area.insert('end', "Comune"+'\n', "comuneP")
    text_area.insert('end', info_provenienza[2]+'\n')
    text_area.insert('end', "Provincia"+'\n', "provinciaP")
    text_area.insert('end', info_provenienza[3]+'\n')

    text_area.insert('end', '\n'+"---- Autore ----"+'\n\n', "autore")
    text_area.insert('end', "Nome"+'\n', "nomeA")
    text_area.insert('end', info_opera[7]+'\n')

    text_area.insert('end', '\n'+"---- Laboratorio ----"+'\n\n', "lab")
    text_area.insert('end', "Nome"+'\n', "nomeL")
    text_area.insert('end', info_laboratorio[1]+'\n')
    text_area.insert('end', "Data Invio"+'\n', "invioL")
    text_area.insert('end', str(info_laboratorio[2])+'\n')

    text_area.insert('end', '\n'+"---- Articoli ----"+'\n\n', "articoli")

    for element in info_citazioni:
        tupl = tuple(element)
        text_area.insert('end', "Articolo"+'\n', "articolo")
        text_area.insert('end', tupl[0][1]+'\n')
        text_area.insert('end', "Nome Pubblicatore"+'\n', "nomePub")
        text_area.insert('end', tupl[0][2]+'\n')
        text_area.insert('end', "Data"+'\n', "dataPub")
        text_area.insert('end', str(tupl[0][3])+'\n')
        text_area.insert('end', "Link"+'\n', "linkPub")
        text_area.insert('end', tupl[0][4]+'\n')
        

        temp4 = []
        for record in my_connession.GetRecord(2, tupl[0][0]):
            temp4.append(record[1])

        info_relatori = []
        for record in temp4:
            info_relatori.append(my_connession.GetRecord(7, record))
            
        for element in info_relatori:
            tupl1 = tuple(element)
            text_area.insert('end', "Nome Relatore"+'\n', "nomeR")
            text_area.insert('end', tupl1[0][1]+'\n')
            text_area.insert('end', "Afferenza"+'\n', "afferenzaR")
            text_area.insert('end', tupl1[0][2]+'\n')

        text_area.insert('end', '\n\n')

    text_area.tag_config('campione', font='Courier 15 bold')
    text_area.tag_config('nomeC', font='Courier 14')
    text_area.tag_config('dataP', font='Courier 14')
    text_area.tag_config('dataC', font='Courier 14')
    text_area.tag_config('luogoC', font='Courier 14')
    text_area.tag_config('stato', font='Courier 14') 
    text_area.tag_config('descrizione', font='Courier 14')
    text_area.tag_config('opera', font='Courier 15 bold')    
    text_area.tag_config('nomeO', font='Courier 14')  
    text_area.tag_config('periodo', font='Courier 14')
    text_area.tag_config('tipologia', font='Courier 14')
    text_area.tag_config('provenienza', font='Courier 15 bold')
    text_area.tag_config('nomeP', font='Courier 14')   
    text_area.tag_config('comuneP', font='Courier 14')
    text_area.tag_config('provinciaP', font='Courier 14') 
    text_area.tag_config('autore', font='Courier 15 bold')
    text_area.tag_config('nomeA', font='Courier 14')  
    text_area.tag_config('lab', font='Courier 15 bold') 
    text_area.tag_config('nomeL', font='Courier 14')
    text_area.tag_config('invioL', font='Courier 14')
    text_area.tag_config('articoli', font='Courier 15 bold')
    text_area.tag_config('articolo', font='Courier 14')
    text_area.tag_config('nomePub', font='Courier 14')
    text_area.tag_config('dataPub', font='Courier 14')
    text_area.tag_config('linkPub', font='Courier 14')
    text_area.tag_config('relatore', font='Courier 15 bold')
    text_area.tag_config('nomeR', font='Courier 14')
    text_area.tag_config('afferenzaR', font='Courier 14')

    

    text_area.configure(state ='disabled')

    



#UI del popup di inserimento
def Insert():
    popup = tk.Toplevel()
    popup.geometry("450x650")
    popup.title("Inserimento")
    my_connession = connection.MyConnector()
    
    global frame_counter
    frame_counter = 0

    query_list = []

    def next():
        global frame_counter 
        frame_counter = min(frame_counter + 1, 3)

    def prev():
        global frame_counter 
        frame_counter = max(frame_counter - 1, 0)

    def NextFrame():
        frames = [frame1, frame2, frame3, frame4]
        frames[frame_counter].grid_forget()
        next()
        frames[frame_counter].grid()
        if frame_counter == 1:
            list.bind('<<ListboxSelect>>',CurSelet)
        else:
            list.unbind('<<ListboxSelect>>')

    def PrevFrame():
        frames = [frame1, frame2, frame3, frame4]
        frames[frame_counter].grid_forget()
        prev()
        frames[frame_counter].grid()
        if frame_counter == 1:
            list.bind('<<ListboxSelect>>',CurSelet)
        else:
            list.unbind('<<ListboxSelect>>')

    def Cancel():
        popup.destroy()

    def Save():

        query_list.append(nomeC.get())
        query_list.append(dataP.get())
        query_list.append(dataC.get())
        query_list.append(luogoC.get())
        query_list.append(stato.get())
        query_list.append(descrizione.get("1.0",'end-1c'))
        query_list.append(nomeO.get())
        query_list.append(periodo.get())
        query_list.append(tipologia.get())
        query_list.append(autore.get())
        query_list.append(provenienza.get())
        query_list.append(comune.get())
        query_list.append(provincia.get())
        query_list.append(lab.get())
        query_list.append(invioLab.get())
        query_list.append(articolo.get())
        query_list.append(nomePub.get())
        query_list.append(dataPub.get())
        query_list.append(link.get())
        query_list.append(relatore.get())
        query_list.append(afferenzaR.get())

        for index in enumerate(query_list):
            if query_list[index[0]] == "":
                query_list[index[0]] = "---" 
                pass

        my_connession.AddEntry(query_list)
        popup.destroy()

        

    frame1 = tk.Frame(popup)
    tk.Label(frame1, text="Nome Campione", width=25).grid(row=1, column = 0, pady = 10)
    nomeC = tk.Entry(frame1, width=25)
    nomeC.grid(row=1, column=1, padx=20, pady = 10)

    tk.Label(frame1, text="Data Prelievo").grid(row=2, column = 0, pady = 10)
    dataP = tk.Entry(frame1, width=25)
    dataP.grid(row=2, column=1, padx=20, pady = 10)
    dataP.insert('end', '0000-00-00')

    tk.Label(frame1, text="Data Catalogazione").grid(row=3, column = 0, pady = 10)
    dataC = tk.Entry(frame1, width=25)
    dataC.grid(row=3, column=1, padx=20, pady = 10)
    dataC.insert('end', date.today())

    tk.Label(frame1, text="Luogo Catalogazione").grid(row=4, column = 0, pady = 10)
    luogoC = tk.Entry(frame1, width=25)
    luogoC.grid(row=4, column=1, padx=20, pady = 10)

    tk.Label(frame1, text="Stato").grid(row=5, column = 0, pady = 10)
    stato = tk.Entry(frame1, width=25)
    stato.grid(row=5, column=1, padx=20, pady = 10)

    tk.Label(frame1, text="Descrizione").grid(row=6, column = 0, pady = 10)
    descrizione = tk.Text(frame1, width=19)
    descrizione.grid(row=6, column=1, padx=20, pady = 10)

    tk.Button(frame1, text='Next', command=NextFrame).grid(row=7, column=1, padx=30, pady = 10, ipadx = 20)
    tk.Button(frame1, text='Cancel', command=Cancel).grid(row=7, column=0, padx=30, pady = 10, ipadx = 20)
    frame1.grid()


    frame2 = tk.Frame(popup)

    tk.Label(frame2, text="").grid(row=0, column = 0, pady = 22)

    tk.Label(frame2, text="Nome Opera", width=25).grid(row=1, column = 0, pady = 10)
    nomeO = tk.Entry(frame2, width=25)
    nomeO.grid(row=1, column=1, padx=20, pady = 10)

    tk.Label(frame2, text="Periodo").grid(row=2, column = 0, pady = 10)
    periodo = tk.Entry(frame2, width=25)
    periodo.grid(row=2, column=1, padx=20, pady = 10)

    tk.Label(frame2, text="Tipologia").grid(row=3, column = 0, pady = 10)
    tipologia = tk.Entry(frame2, width=25)
    tipologia.grid(row=3, column=1, padx=20, pady = 10)

    tk.Label(frame2, text="Autore").grid(row=4, column = 0, pady = 10)
    autore = tk.Entry(frame2, width=25)
    autore.grid(row=4, column=1, padx=20, pady = 10)

    tk.Label(frame2, text="").grid(row=5, column = 0, pady = 46)
    list = tk.Listbox(frame2, selectmode = "single")
    list.grid(row=6, columnspan=2, sticky='e', ipadx=112, ipady=30)

    temp = []
    for record in my_connession.GetRecord(1):
        temp.append(record)
        list.insert('end', record[1])
    
    def CurSelet(event):
        nomeO.delete(0, 'end')
        periodo.delete(0, 'end')
        tipologia.delete(0, 'end')
        autore.delete(0, 'end')
        provenienza.delete(0, 'end')
        comune.delete(0, 'end')
        provincia.delete(0, 'end')

        row = list.curselection()
        temp1 = temp[row[0]]

        nomeO.insert('end', temp1[1])
        periodo.insert('end', temp1[2])
        tipologia.insert('end', temp1[3])
        autore.insert('end', temp1[7])
        prov = my_connession.GetRecord(4, temp1[5])
        provenienza.insert('end', prov[0][1])
        comune.insert('end', prov[0][2])
        provincia.insert('end', prov[0][3])

    tk.Label(frame2, text="").grid(row=7, column = 0, pady = 13)
    tk.Button(frame2, text='Next', command=NextFrame).grid(row=8, column=1, padx=30, pady = 10, ipadx = 20)
    tk.Button(frame2, text='Prev', command=PrevFrame).grid(row=8, column=0, padx=30, pady = 10, ipadx = 20)


    frame3 = tk.Frame(popup)

    tk.Label(frame3, text="").grid(row=0, column = 0, pady = 22)

    tk.Label(frame3, text="Provenienza", width=25).grid(row=1, column = 0, pady = 10)
    provenienza = tk.Entry(frame3, width=25)
    provenienza.grid(row=1, column=1, padx=20, pady = 10)

    tk.Label(frame3, text="Comune").grid(row=2, column = 0, pady = 10)
    comune = tk.Entry(frame3, width=25)
    comune.grid(row=2, column=1, padx=20, pady = 10)

    tk.Label(frame3, text="Provincia").grid(row=3, column = 0, pady = 10)
    provincia = tk.Entry(frame3, width=25)
    provincia.grid(row=3, column=1, padx=20, pady = 10)

    tk.Label(frame3, text="").grid(row=4, column = 0, pady = 50)

    tk.Label(frame3, text="Laboratorio", width=25).grid(row=5, column = 0, pady = 10)
    lab = tk.Entry(frame3, width=25)
    lab.grid(row=5, column=1, padx=20, pady = 10)

    tk.Label(frame3, text="Inviato il").grid(row=6, column = 0, pady = 10)
    invioLab = tk.Entry(frame3, width=25)
    invioLab.grid(row=6, column=1, padx=20, pady = 10)
    invioLab.insert('end', '0000-00-00')

    tk.Label(frame3, text="").grid(row=7, column = 0, pady = 100)

    tk.Button(frame3, text='Next', command=NextFrame).grid(row=8, column=1, padx=20, pady = 10, ipadx = 20)
    tk.Button(frame3, text='Prev', command=PrevFrame).grid(row=8, column=0, padx=20, pady = 10, ipadx = 20)


    frame4 = tk.Frame(popup)

    tk.Label(frame4, text="").grid(row=0, column = 0, pady = 22)

    tk.Label(frame4, text="Articolo", width=25).grid(row=1, column = 0, pady = 10)
    articolo = tk.Entry(frame4, width=25)
    articolo.grid(row=1, column=1, padx=20, pady = 10)

    tk.Label(frame4, text="Nome Pubblicatore").grid(row=2, column = 0, pady = 10)
    nomePub = tk.Entry(frame4, width=25)
    nomePub.grid(row=2, column=1, padx=20, pady = 10)

    tk.Label(frame4, text="Data Pubblicazione").grid(row=3, column = 0, pady = 10)
    dataPub = tk.Entry(frame4, width=25)
    dataPub.grid(row=3, column=1, padx=20, pady = 10)
    dataPub.insert('end', '0000-00-00')

    tk.Label(frame4, text="Link").grid(row=4, column = 0, pady = 10)
    link = tk.Entry(frame4, width=25)
    link.grid(row=4, column=1, padx=20, pady = 10)

    tk.Label(frame4, text="").grid(row=5, column = 0, pady = 100)

    tk.Label(frame4, text="Relatore").grid(row=6, column = 0, pady = 10)
    relatore = tk.Entry(frame4, width=25)
    relatore.grid(row=6, column=1, padx=20, pady = 10)

    tk.Label(frame4, text="Afferenza").grid(row=7, column = 0, pady = 10)
    afferenzaR = tk.Entry(frame4, width=25)
    afferenzaR.grid(row=7, column=1, padx=20, pady = 10)

    tk.Label(frame4, text="").grid(row=8, column = 0, pady = 94)

    tk.Button(frame4, text='Save', command=Save).grid(row=8, column=1, padx=20, pady = 10, ipadx = 20)
    tk.Button(frame4, text='Prev', command=PrevFrame).grid(row=8, column=0, padx=20, pady = 10, ipadx = 20)

    return query_list