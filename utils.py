import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

#Tanta roba, ma serve solo per fare la UI del popup
def Popup(item):
    popup = tk.Toplevel()
    popup.geometry("450x650")
    popup.title("Dettagli")

    for value in item:
        print("\n" + str(value))

    campione = "---- Campione ----"
    nomeC = "Nome"
    dataP = "Data Prelievo"
    dataC = "Data Catalogazione"
    luogoC = "Luogo Catalogazione"
    stato = "Stato"
    descrizione = "Descrizione"

    opera = "---- Opera ----"
    nomeO = "Opera"
    periodo = "Periodo"
    tipologia = "Tipologia"

    provenienza = "---- Provenienza ----"
    nomeP = "Nome"
    comuneP = "Comune"
    provinciaP = "Provincia"

    autore = "--- Autore ----"
    nomeA = "Nome"

    laboratorio = "---- Laboratorio ----"
    nomeL = "Nome"
    invioL = "Data Invio"

    articoli = "---- Articoli ----"
    nomePub = "Nome Pubblicatore"
    dataPub = "Data"
    linkPub = "Link"

    relatore = "---- Relatore ----"
    nomeR = "Nome"
    afferenzaR = "Afferenza"


    text_area = scrolledtext.ScrolledText(popup, spacing3 = 2, wrap = tk.WORD, width = 440, height = 640, font = ("Courier", 10))
    text_area.pack(fill='both')
    
    text_area.focus()

    text_area.insert('end', campione+'\n\n')
    text_area.insert('end', nomeC+'\n')
    text_area.insert('end', item[0]+'\n')
    text_area.insert('end', dataP+'\n')
    text_area.insert('end', dataP+'\n')
    text_area.insert('end', dataC+'\n')
    text_area.insert('end', dataC+'\n')
    text_area.insert('end', luogoC+'\n')
    text_area.insert('end', luogoC+'\n')
    text_area.insert('end', stato+'\n')
    text_area.insert('end', stato+'\n')
    text_area.insert('end', descrizione+'\n')
    text_area.insert('end', item[1]+'\n')

    text_area.insert('end', '\n'+opera+'\n\n')
    text_area.insert('end', nomeO+'\n')
    text_area.insert('end', nomeO+'\n')
    text_area.insert('end', periodo+'\n')
    text_area.insert('end', periodo+'\n')
    text_area.insert('end', tipologia+'\n')
    text_area.insert('end', tipologia+'\n')

    text_area.insert('end', '\n'+provenienza+'\n\n')
    text_area.insert('end', nomeP+'\n')
    text_area.insert('end', nomeP+'\n')
    text_area.insert('end', comuneP+'\n')
    text_area.insert('end', comuneP+'\n')
    text_area.insert('end', provinciaP+'\n')
    text_area.insert('end', provinciaP+'\n')

    text_area.insert('end', '\n'+autore+'\n\n')
    text_area.insert('end', nomeA+'\n')
    text_area.insert('end', nomeA+'\n')

    text_area.insert('end', '\n'+laboratorio+'\n\n')
    text_area.insert('end', nomeL+'\n')
    text_area.insert('end', nomeL+'\n')
    text_area.insert('end', invioL+'\n')
    text_area.insert('end', invioL+'\n')

    text_area.insert('end', '\n'+articoli+'\n\n')
    text_area.insert('end', nomePub+'\n')
    text_area.insert('end', nomePub+'\n')
    text_area.insert('end', dataPub+'\n')
    text_area.insert('end', dataPub+'\n')
    text_area.insert('end', linkPub+'\n')
    text_area.insert('end', linkPub+'\n')

    text_area.insert('end', '\n'+relatore+'\n\n')
    text_area.insert('end', nomeR+'\n')
    text_area.insert('end', nomeR+'\n')
    text_area.insert('end', afferenzaR+'\n')
    text_area.insert('end', afferenzaR+'\n')


    
    text_area.tag_add('campione','1.0','1.end')
    text_area.tag_config('campione', font='Courier 15 bold')

    text_area.tag_add('nomeC','3.0','3.end')
    text_area.tag_config('nomeC', font='Courier 14')
    text_area.tag_add('dataP','5.0','5.end')
    text_area.tag_config('dataP', font='Courier 14')
    text_area.tag_add('dataC','7.0','7.end')
    text_area.tag_config('dataC', font='Courier 14')
    text_area.tag_add('luogoC','9.0','9.end')
    text_area.tag_config('luogoC', font='Courier 14')
    text_area.tag_add('stato','11.0','11.end')
    text_area.tag_config('stato', font='Courier 14') 
    text_area.tag_add('descrizione','13.0','13.end')
    text_area.tag_config('descrizione', font='Courier 14')

    text_area.tag_add('opera','16.0','16.end')
    text_area.tag_config('opera', font='Courier 15 bold')    
    
    text_area.tag_add('nomeO','18.0','18.end')
    text_area.tag_config('nomeO', font='Courier 14')  
    text_area.tag_add('periodo','20.0','20.end')
    text_area.tag_config('periodo', font='Courier 14')
    text_area.tag_add('tipologia','22.0','22.end')
    text_area.tag_config('tipologia', font='Courier 14')

    text_area.tag_add('provenienza','25.0','25.end')
    text_area.tag_config('provenienza', font='Courier 15 bold')

    text_area.tag_add('nomeP','27.0','27.end')
    text_area.tag_config('nomeP', font='Courier 14')   
    text_area.tag_add('comuneP','29.0','29.end')
    text_area.tag_config('comuneP', font='Courier 14')
    text_area.tag_add('provinciaP','31.0','31.end')
    text_area.tag_config('provinciaP', font='Courier 14') 

    text_area.tag_add('autore','34.0','34.end')
    text_area.tag_config('autore', font='Courier 15 bold')
    text_area.tag_add('nomeA','36.0','36.end')
    text_area.tag_config('nomeA', font='Courier 14')  

    text_area.tag_add('lab','39.0','39.end')
    text_area.tag_config('lab', font='Courier 15 bold') 

    text_area.tag_add('nomeL','41.0','41.end')
    text_area.tag_config('nomeL', font='Courier 14')
    text_area.tag_add('invioL','43.0','43.end')
    text_area.tag_config('invioL', font='Courier 14')

    text_area.tag_add('articoli','46.0','46.end')
    text_area.tag_config('articoli', font='Courier 15 bold')

    text_area.tag_add('nomePub','48.0','48.end')
    text_area.tag_config('nomePub', font='Courier 14')
    text_area.tag_add('dataPub','50.0','50.end')
    text_area.tag_config('dataPub', font='Courier 14')
    text_area.tag_add('linkPub','52.0','52.end')
    text_area.tag_config('linkPub', font='Courier 14')

    text_area.tag_add('relatore','55.0','55.end')
    text_area.tag_config('relatore', font='Courier 15 bold')

    text_area.tag_add('nomeR','57.0','57.end')
    text_area.tag_config('nomeR', font='Courier 14')
    text_area.tag_add('afferenzaR','59.0','59.end')
    text_area.tag_config('afferenzaR', font='Courier 14')



    text_area.configure(state ='disabled')

