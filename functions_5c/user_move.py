# Functions for main
from tkinter import *


def wzrok():
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()

    t1 = Checkbutton(text='Kolory', variable=var1, onvalue=1, offvalue=0, command=lambda: f_ch_1(var1))
    t1.pack()
    t2 = Checkbutton(text='Proporcje', variable=var2, onvalue=1, offvalue=0, command=lambda: f_ch_2(var2))
    t2.pack()
    t3 = Checkbutton(text='Absurdalne', variable=var3, onvalue=1, offvalue=0, command=lambda: f_ch_3(var3))
    t3.pack()
    t4 = Checkbutton(text='Niespotykane', variable=var4, onvalue=1, offvalue=0, command=lambda: f_ch_4(var4))
    t4.pack()


def f_ch_1(var1):
    if var1.get() == 1:
        e1 = Entry(fg='Blue')
        e1.pack()
        l1 = Label(text='Tutaj wyświetli się odpowiedź')
        l1.pack()
        b_ok = Button(text='OK', command=lambda: f_answer_1(e1, l1))
        b_ok.pack()
    else:
        pass


def f_answer_1(e1, l1):
    if e1.get() == 'jaskrawe' or e1.get() == 'niecodzienne':
        l1.config(text='Dobrze')
    else:
        l1.config(text='Żle')


def f_ch_2(var2):
    if var2.get() == 1:
        e2 = Entry(fg='Blue')
        e2.pack()
        l2 = Label(text='Tutaj wyświetli się odpowiedź')
        l2.pack()
        b_ok = Button(text='OK', command=lambda: f_answer_2(e2, l2))
        b_ok.pack()
    else:
        pass


def f_answer_2(e2, l2):
    if e2.get() == 'małe' or e2.get() == 'gigantyczne':
        l2.config(text='Dobrze')
    else:
        l2.config(text='Żle')


def f_ch_3(var3):
    if var3.get() == 1:
        e3 = Entry(fg='Blue')
        e3.pack()
        l3 = Label(text='Tutaj wyświetli się odpowiedź')
        l3.pack()
        b_ok = Button(text='OK', command=lambda: f_answer_3(e3, l3))
        b_ok.pack()
    else:
        pass


def f_answer_3(e3, l3):
    if e3.get() == 'daleko' or e3.get() == 'blisko':
        l3.config(text='Dobrze')
    else:
        l3.config(text='Żle')


def f_ch_4(var4):
    if var4.get() == 1:
        e4 = Entry(fg='Blue')
        e4.pack()
        l4 = Label(text='Tutaj wyświetli się odpowiedź')
        l4.pack()
        b_ok = Button(text='OK', command=lambda: f_answer_4(e4, l4))
        b_ok.pack()
    else:
        pass


def f_answer_4(e4, l4):
    if e4.get() == 'dużo' or e4.get() == 'mało':
        l4.config(text='Dobrze')
    else:
        l4.config(text='Żle')
