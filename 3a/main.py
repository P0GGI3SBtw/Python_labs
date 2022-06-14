from tkinter import *
import os


def operators():
    try:
        n1 = int(Entry.get(a))
        n2 = int(Entry.get(b))

        if var_o.get() == 0:
            result = n1 + n2
        elif var_o.get() == 1:
            result = n1 - n2

        res_l.config(text=f'Wynik to: {result}')

        return result
    except ValueError as e:
        print(e)


def zapis():
    os.chdir('wynik')

    file = open('result.txt', 'w')
    file.write(f'Wynik to: {operators()}')
    file.close()


app = Tk()
app.title('Calculator')
app.geometry('250x300')

var_a = IntVar()
var_b = IntVar()
var_o = IntVar()

a = Scale(app, from_=0, to=100, tickinterval=25, variable=var_a)
a.grid(row=1, column=1)

b = Entry(app, textvariable=var_b)
b.grid(row=2, column=1)

plus = Radiobutton(app, text='+', variable=var_o, value=0)
plus.grid(row=2, column=2)

minus = Radiobutton(app, text='-', variable=var_o, value=1)
minus.grid(row=3, column=2)

res_l = Label(app, text='Wynik: 0')
res_l.grid(row=4, column=1)

ok_b = Button(text='OK', command=operators)
ok_b.grid(row=3, column=1)

z_b = Button(text='Zapisz', command=zapis)
z_b.grid(row=5, column=1)

app.mainloop()
