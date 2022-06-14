import os
from tkinter import *


def save():
    try:
        int(ilosc.get())

        if int(t_var.get()) > 10:
            os.chdir('wynik')
            file = open('wyraz.txt', 'w')
            for i in range(t_var.get()):
                file.write(w_var.get())
                file.write('\n')
            file.close()
        else:
            pass
    except ValueError as e:
        print(e)


app = Tk()
app.title('My app')
app.geometry('350x300')

w_var = StringVar()
t_var = IntVar()

Label(app, text='Podaj ile razy chcesz wypisać wyraz').grid(row=1, column=1)
ilosc = Entry(app, textvariable=t_var)
ilosc.grid(row=1, column=2)

Label(app, text='Podaj wyraz').grid(row=2, column=1)
Entry(app, textvariable=w_var).grid(row=2, column=2)

Button(app, text='Zapisz', command=save).grid(row=3, column=1)

app.mainloop()
