from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pywhatkit

#cor

branco = '#ffffff'
azul = ('#364a85')

#----------------------------------------------------------------------------------------------------------------
#tela
tela1 =Tk()
tela1.title('ASCII Art')
tela1.geometry('700x900+400+100')
tela1.wm_resizable(width=False, height=False)

#função
def open():

    global filename

    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select your Image...',
    filetypes= (('PNG file', '*.png'), ('JPG file', '*.jpg')))

def coverter():

    global filename

    ler= pywhatkit.image_to_ascii_art(filename)

    #label
    lb_converter = Label(tela1, text=ler, font='Time 6', anchor=N)
    lb_converter.place(width=650, height=800, x=50, y=100)

def salvar():

    global filename

    pywhatkit.image_to_ascii_art(filename, 'Exemple')
    messagebox.showinfo("Information", "Saved 'Example.txt' in your folder")

#label e entrys
lb_title = Label(tela1, text='ASCII Art', font= 'Time 20 bold', bg = azul, fg= branco, anchor='w', padx=260)

#butoes

b_open = Button(tela1, text='Open', command=open, font='Time 10 bold', bg=branco, fg= azul)
b_open.place(width=85, height=30, x=100, y=70, )

b_converter = Button(tela1, text='Converter', command =coverter , font='Time 10 bold', bg=branco, fg= azul)
b_converter.place(width=85, height=30, x=300, y=70, )

b_salvar = Button(tela1, text='Save', command=salvar, font='Time 10 bold', bg=branco, fg= azul)
b_salvar.place(width=85, height=30, x=500, y=70, )

tela1.mainloop()