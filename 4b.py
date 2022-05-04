from tkinter import *


def add():
    print('Podsumowanie:\n'
          'Agd: {}\n'
          'Kosmetyki {}\n'
          'Odzież {}'.format(agd.get(), kos.get(), odz.get()))


app = Tk()
app.geometry('200x300')
agd = IntVar()
kos = IntVar()
odz = IntVar()

agd_label = Label(text='Agd:')
agd_label.grid(row=1, column=1)
slide1 = Scale(app, from_=0, to=1, tickinterval=1, variable=agd)
slide1.set(value=0)
slide1.grid(row=2, column=1)

kos_label = Label(text='Kosmetyki:')
kos_label.grid(row=1, column=2)
slide2 = Scale(app, from_=0, to=1, tickinterval=1, variable=kos)
slide2.set(value=0)
slide2.grid(row=2, column=2)

odz_label = Label(text='Odzież:')
odz_label.grid(row=1, column=3)
slide2 = Scale(app, from_=0, to=1, tickinterval=1, variable=odz)
slide2.set(value=0)
slide2.grid(row=2, column=3)

button_ok = Button(app, text='Koniec ankiety', fg='green', command=add)
button_ok.grid(row=3, column=1)

app.mainloop()
